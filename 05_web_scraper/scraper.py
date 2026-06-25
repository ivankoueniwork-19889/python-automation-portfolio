"""
Web Scraper with Rate Limiting
==============================
Scrapes book data from books.toscrape.com including title, price,
star rating, and availability. Respects rate limits between requests
and saves all results to a CSV file.

This script follows the professional web scraping process:
  1. Check robots.txt before making any requests
  2. Fetch pages with retry logic and randomized delays
  3. Parse HTML using CSS class selectors
  4. Paginate automatically until max pages reached
  5. Save structured output to CSV with timestamps

Usage:
    python scraper.py

Example:
    python scraper.py

Author : ivankoueniwork-19889
Script : 05 / 10
"""

# ─── Standard library imports ─────────────────────────────────────────────────
import csv                              # writes structured data to CSV files
from datetime import datetime           # timestamps for each scraped record
import logging                          # structured output with severity levels
from pathlib import Path                # modern file path handling
import random                           # randomized delays between requests
import time                             # rate limiting — pauses between requests
from urllib.parse import urljoin        # builds absolute URLs from relative hrefs
from urllib.robotparser import RobotFileParser  # parses and checks robots.txt rules

# ─── Third party imports ──────────────────────────────────────────────────────
import httpx                            # modern HTTP client for making requests
from bs4 import BeautifulSoup          # HTML parser for extracting structured data


# ─── Logging configuration ────────────────────────────────────────────────────
# Configured once at the top level before any functions run.
# Using logging instead of print() gives every message a timestamp and
# severity level — essential when processing many pages and debugging failures.
#
# Level INFO shows: INFO, WARNING, ERROR, CRITICAL (hides DEBUG noise)
#
# Format breakdown:
#   %(asctime)s      → timestamp    : 23:51:58
#   %(levelname)-8s  → severity     : INFO     (padded to 8 chars)
#   %(message)s      → our message  : Parsed 20 books from page
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)

# Standard logger pattern — named after this module for traceability
log = logging.getLogger(__name__)


# ─── Configuration constants ──────────────────────────────────────────────────
# Defined once here so the script is easy to reconfigure without
# touching any function logic. ALL_CAPS signals these never change at runtime.

BASE_URL    = "http://books.toscrape.com/"  # target website to scrape
OUTPUT_FILE = Path("output/books.csv")      # destination for scraped data
DELAY_MIN   = 1                             # minimum seconds between requests
DELAY_MAX   = 3                             # maximum seconds between requests
MAX_RETRIES = 2                             # retry attempts before giving up
MAX_PAGES   = 5                             # number of pages to scrape per run


# ─── Functions ────────────────────────────────────────────────────────────────

def check_robots(url: str) -> bool:
    """Check robots.txt to verify the target URL is allowed to be scraped.

    Uses Python's built-in RobotFileParser to fetch and parse the robots.txt
    file for the given domain. This is the professional and ethical first step
    before making any scraping requests.

    Parameters
    ----------
    url : str
        Base URL of the website to check.

    Returns
    -------
    bool
        True if scraping is allowed, False if blocked by robots.txt.
        Returns True if robots.txt cannot be read — assumes allowed.
    """
    rp = RobotFileParser()
    # Point the parser at the robots.txt file for this domain
    rp.set_url(urljoin(url, "robots.txt"))

    try:
        # Read and parse the robots.txt rules
        rp.read()
    except Exception as e:
        # If we can't read robots.txt, log a warning and proceed
        # This handles sites with no robots.txt or network errors
        log.warning(f"Could not read robots.txt: {e} — proceeding anyway")
        return True

    # can_fetch("*", url) checks rules for all user agents against our URL
    allowed = rp.can_fetch("*", url)
    log.info(f"robots.txt check for {url}: {'allowed' if allowed else 'blocked'}")
    return allowed


def fetch_page(url: str, retries: int) -> str | None:
    """Fetch the HTML content of a URL with retry logic and rate limiting.

    Attempts the request up to `retries` times. On failure, waits a
    randomized delay before retrying to avoid overwhelming the server.
    Non-retryable errors (404, 400) return None immediately without retrying.

    Parameters
    ----------
    url : str
        Full URL of the page to fetch.
    retries : int
        Maximum number of attempts before returning None.

    Returns
    -------
    str | None
        Raw HTML string on success, None if all retries are exhausted
        or a non-retryable error is encountered.
    """
    while retries > 0:
        try:
            # Send GET request — follow_redirects handles HTTP → HTTPS redirects
            response = httpx.get(url, timeout=10, follow_redirects=True)
            log.info(f"Status: {response.status_code} — {url}")

            # Non-retryable errors — page doesn't exist or bad URL
            # Retrying won't help so we return None immediately
            if response.status_code in (404, 400):
                log.warning(f"Non-retryable error {response.status_code} — skipping")
                return None

            # Success — return the raw HTML
            return response.text

        except Exception as e:
            # Network error, timeout, or connection failure — retryable
            retries -= 1
            log.warning(f"Could not fetch page: {e} — {retries} retries left")

            # Randomized delay looks more human and avoids triggering rate limits
            delay = random.uniform(DELAY_MIN, DELAY_MAX)
            log.info(f"Waiting {delay:.1f}s before next request...")
            time.sleep(delay)

    # All retries exhausted — signal failure to the caller
    return None


def parse_books(html: str) -> list[dict]:
    """Extract book data from a page of HTML.

    Parses the HTML using BeautifulSoup and extracts title, price,
    star rating, and availability for every book on the page.

    HTML structure reference:
        <article class="product_pod">
            <p class="star-rating Three">       ← rating in class name
            <h3><a title="Book Title">          ← title in attribute
            <p class="price_color">£51.77       ← price as text
            <p class="instock availability">    ← availability as text

    Parameters
    ----------
    html : str
        Raw HTML string from fetch_page().

    Returns
    -------
    list[dict]
        List of book dicts with keys: title, price, rating, availability.
    """
    result = []
    soup = BeautifulSoup(html, "html.parser")

    # Find every book on the page — each lives in an <article class="product_pod">
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        result.append({
            # Title lives in the 'title' attribute of the <a> tag, not its text
            "title":        book.find("h3").find("a")["title"],
            # Price text may have leading/trailing whitespace — strip it
            "price":        book.find("p", class_="price_color").text.strip(),
            # Rating is encoded as the second CSS class: "star-rating Three"
            # index [1] gets "Three", "One", "Two" etc.
            "rating":       book.find("p", class_="star-rating")["class"][1],
            # Availability text may have newlines — strip cleans it up
            "availability": book.find("p", class_="instock availability").text.strip(),
        })

    log.info(f"Parsed {len(result)} books from page")
    return result


def get_next_page(html: str, base_url: str) -> str | None:
    """Find the URL of the next page if one exists.

    Looks for the pagination next button in the HTML. If found, builds
    and returns the full absolute URL for the next page.

    Parameters
    ----------
    html : str
        Raw HTML of the current page.
    base_url : str
        Base URL used to convert relative hrefs to absolute URLs.

    Returns
    -------
    str | None
        Full URL of the next page, or None if this is the last page.
    """
    soup = BeautifulSoup(html, "html.parser")

    # The next button is an <li class="next"> containing an <a href="...">
    next_button = soup.find("li", class_="next")

    if next_button:
        # Get the relative href from the <a> tag inside the next button
        next_page = next_button.find("a")["href"]
        # urljoin builds the full absolute URL from the relative href
        return urljoin(base_url, next_page)

    # No next button found — this is the last page
    return None


def save_to_csv(books: list[dict], path: Path) -> None:
    """Save the list of scraped books to a CSV file.

    Creates the output directory if it does not exist, then writes
    a header row followed by all book records using DictWriter.

    Parameters
    ----------
    books : list[dict]
        List of book dicts to write. Each must contain all six column keys.
    path : Path
        Destination file path for the CSV output.
    """
    # Create the output/ folder if it doesn't exist yet
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "title", "price", "rating",
            "availability", "page_number", "scraped_at"
        ])
        # Write the column header row first
        writer.writeheader()
        # Write all book records in one call
        writer.writerows(books)

    log.info(f"Saved {len(books)} books to {path}")


def scrape(base_url: str, max_pages: int) -> None:
    """Orchestrate the full scraping pipeline.

    Checks robots.txt, then paginates through up to max_pages pages,
    extracting books from each and accumulating them into a master list.
    Adds page number and timestamp to every record before saving to CSV.

    Parameters
    ----------
    base_url : str
        Starting URL — the first page to scrape.
    max_pages : int
        Maximum number of pages to scrape per run.
    """
    # Step 1 — always check robots.txt before making any requests
    is_scrapable = check_robots(base_url)
    if not is_scrapable:
        log.warning("Scraping blocked by robots.txt — exiting")
        return

    # Master list accumulates books from all pages
    all_books = []
    # Track current page number for the CSV page_number column
    page_number = 1

    while max_pages > 0:
        # Step 2 — fetch the HTML for the current page
        page_html = fetch_page(base_url, MAX_RETRIES)

        # If fetch failed after all retries, stop the run
        if not page_html:
            log.warning(f"Skipping page {page_number} — could not fetch")
            break

        # Step 3 — extract all books from this page
        books = parse_books(page_html)

        # Step 4 — enrich each book record with metadata
        for book in books:
            # Page number tells the analyst which page this book came from
            book["page_number"] = page_number
            # Timestamp tells the analyst when this data was collected
            book["scraped_at"]  = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Add this page's books to the master collection
        all_books.extend(books)
        log.info(f"Page {page_number} — {len(books)} books collected")

        # Step 5 — find the next page URL
        # None means we have reached the last page
        base_url = get_next_page(page_html, base_url)
        if not base_url:
            log.info("No more pages — scraping complete")
            break

        # Move counters forward for next iteration
        max_pages -= 1
        page_number += 1

    # Step 6 — save all collected books to CSV
    save_to_csv(all_books, OUTPUT_FILE)


# ─── Entry point ──────────────────────────────────────────────────────────────
def main() -> None:
    """Parse command-line arguments and run the scraper."""
    log.info(f"Starting scraper — target: {BASE_URL}")
    scrape(BASE_URL, MAX_PAGES)
    log.info("Scraping complete")


# ─── Guard ────────────────────────────────────────────────────────────────────
# Only runs when executed directly — not when imported by another module.
if __name__ == "__main__":
    main()

