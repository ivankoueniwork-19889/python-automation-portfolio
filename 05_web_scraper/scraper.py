"""
Web Scraper with Rate Limiting
==============================
Scrapes book data from books.toscrape.com including title, price,
star rating, and availability. Respects rate limits between requests
and saves results to a CSV file.

Usage:
    python scraper.py

Example:
    python scraper.py

Author : ivankoueniwork-19889
Script : 05 / 10
"""

#Standard library
import csv # saves results to CSV file
from datetime import datetime
import logging
from pathlib import Path
import random # randomized delays
import time # rate limiting delays
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
#third party
import httpx # HTTP requests
from bs4 import BeautifulSoup # HTML parsing

# ─── Logging configuration ────────────────────────────────────────────────────
# We configure logging once at the top level, before any functions run.
# Using logging instead of print() gives us timestamps and severity levels
# which are essential when monitoring multiple endpoints simultaneously.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)

# getLogger(__name__) creates a logger named after this module.
# __name__ equals "__main__" when run directly, or the filename when imported.
# This is the standard pattern used in every professional Python codebase.
log = logging.getLogger(__name__)

#the website we're scraping
BASE_URL = "http://books.toscrape.com/"
#where to save the CSV
OUTPUT_FILE = Path("output/books.csv")
#minimum seconds to wait between requests
DELAY_MIN = 1
#maximum seconds to wait between requests
DELAY_MAX = 3
#how many times to retry a failed request
MAX_RETRIES = 2
# Pages to scrape per run
MAX_PAGES = 5



def check_robots(url:str) -> bool:
    """
    Retrieves the robots.txt file for a given domain.
    """
    rp = RobotFileParser()
    rp.set_url(urljoin(url, "robots.txt"))
    
    try:
        rp.read()
    except Exception as e:
        log.warning(f"Could not read robots.txt: {e} — proceeding anyway")
        return True
    
    # Check if our scraper is allowed to access a URL
    allowed = rp.can_fetch("*", url)
    log.info(f"robots.txt check for {url}: {'allowed' if allowed else 'blocked'}")
    return allowed
    
def fetch_page(url:str, retries:int) -> str | None:
    """
    Fetches a URL and returns structured information about the response.
    """
    
    while retries > 0:
        try:
            response = httpx.get(url, timeout=10, follow_redirects=True)
            log.info(f"Status: {response.status_code} — {url}")
            if response.status_code in (404,400):
                log.warning(f"Non-retryable error {response.status_code} — skipping")
                return None 
            return response.text
        except Exception as e:
            retries -= 1
            log.warning(f"Could not fetch page: {e} — {retries} retries left")
            delay = random.uniform(DELAY_MIN, DELAY_MAX)
            log.info(f"Waiting {delay:.1f}s before next request...")
            time.sleep(delay)
            
    return None



def parse_books(html:str) -> list[dict]:
    """extract title, price, rating, and availability per book
    """
    result = []
    soup = BeautifulSoup(html,"html.parser")
    books = soup.find_all("article",class_="product_pod")
    for book in books:
        result.append({
            "title": book.find("h3").find("a")["title"],
            "price": book.find("p",class_="price_color").text.strip(),
            "rating": book.find("p", class_="star-rating")["class"][1],
            "availability":book.find("p",class_="instock availability").text.strip()
            })
    log.info(f"Parsed {len(result)} books from page")
    return result

def get_next_page(html:str, base_url:str) -> str | None:
    """paginate through multiple pages automatically
    """
    
    soup = BeautifulSoup(html,"html.parser")
    next_button = soup.find("li",class_="next")
    if next_button:
        next_page= next_button.find("a")["href"]
        return urljoin(base_url,next_page)
    return None

def save_to_csv(books: list [dict], path: Path) -> None:
    """ save results to a CSV file """
    #Creates output if it does not exist
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path,"w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "rating", "availability", "page_number", "scraped_at"])
        writer.writeheader()
        writer.writerows(books)
    log.info(f"Saved {len(books)} books to {path}")
    
def scrape(base_url: str, max_pages: int) -> None:
    """
    Orchestrate the full scraping pipeline.
    Checks robots.txt, paginates through pages, extracts books,
    and saves all results to CSV.
    """
    # Check robots.txt before doing anything — respect the rules
    is_scrapable = check_robots(base_url)
    if not is_scrapable:
        log.warning("Scraping blocked by robots.txt — exiting")
        return

    # Master list that accumulates books across all pages
    all_books = []

    # Track which page we are on for the CSV output
    page_number = 1

    while max_pages > 0:
        # Fetch the raw HTML for the current page
        page_html = fetch_page(base_url, MAX_RETRIES)

        # Skip this page if fetch failed after all retries
        if not page_html:
            log.warning(f"Skipping page {page_number} — could not fetch")
            break

        # Extract book data from the HTML
        books = parse_books(page_html)

        # Add page number and timestamp to each book record
        for book in books:
            book["page_number"] = page_number
            book["scraped_at"]  = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Add this page's books to the master list
        all_books.extend(books)
        log.info(f"Page {page_number} — {len(books)} books collected")

        # Find the next page URL — None means we are on the last page
        base_url = get_next_page(page_html, base_url)
        if not base_url:
            log.info("No more pages — scraping complete")
            break

        # Move to next page
        max_pages -= 1
        page_number += 1

    # Save all collected books to CSV
    save_to_csv(all_books, OUTPUT_FILE)


def main() -> None:
    """Run the scraper."""
    log.info(f"Starting scraper — target: {BASE_URL}")  # ✅ before
    scrape(BASE_URL, MAX_PAGES)
    log.info("Scraping complete")


if __name__ == "__main__":
    main()
                            