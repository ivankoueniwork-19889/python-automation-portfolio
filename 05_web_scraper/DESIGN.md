Script 05 — Web Scraper with Rate Limiting
==========================================

CONSTANTS
─────────
BASE_URL     → target website
OUTPUT_FILE  → CSV output path  
DELAY_MIN    → minimum wait between requests
DELAY_MAX    → maximum wait between requests
MAX_RETRIES  → retry attempts on failure
MAX_PAGES    → pages to scrape

CORE FUNCTIONS
──────────────
check_robots(url)              → bool
fetch_page(url, retries)       → str | None
parse_books(html)              → list[dict]
get_next_page(html, base_url)  → str | None
save_to_csv(books, path)       → None
scrape(base_url, max_pages)    → None
main()                         → None

ERROR HANDLING
──────────────
Retryable   → 408, 500, 429, network errors
Non-retry   → 404, 400, empty HTML

CSV COLUMNS
───────────
title, price, rating, availability, page_number, scraped_at

STRETCH GOALS
─────────────
Audit logging       → run reports
Schema validation   → detect HTML changes
Pagination chunking → handle 1000+ pages
Auth module         → headers, cookies, API keys