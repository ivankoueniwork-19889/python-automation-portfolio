"""
API Health Monitor
==================
Monitors the health and response time of multiple API endpoints concurrently.
Reads endpoints from a JSON config file, pings each one asynchronously,
and reports status, response time, and any failures in real time.

Usage:
    python monitor.py <endpoints.json>

Example:
    python monitor.py endpoints.json

Author : ivankoueniwork-19889
Script : 04 / 10
"""

# standard library
import argparse
import asyncio
import json
import logging
import time
from pathlib import Path

# third party
import httpx
from rich.console import Console
from rich.table import Table


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

# Console() is rich's output handler — used instead of print() for
# formatted, colored terminal output including tables and styled text.
console = Console()


# ─── Functions ────────────────────────────────────────────────────────────────

def load_endpoints(path: Path) -> list[dict]:
    """Load and return the list of endpoints from a JSON config file."""
    # Open the config file and parse it as a list of endpoint dictionaries.
    # Each dict contains: name, url, and timeout fields.
    with open(path) as file:
        endpoints = json.load(file)
        # Log the count so we can confirm the config loaded correctly
        log.info(f"Loaded {len(endpoints)} endpoint(s) from {path}")
        return endpoints


async def check_endpoint(client: httpx.AsyncClient, endpoint: dict) -> dict:
    """Check a single endpoint and return its status, response time, and result.

    Parameters
    ----------
    client : httpx.AsyncClient
        Shared HTTP client — reused across all checks to avoid
        opening a new connection per endpoint.
    endpoint : dict
        Single endpoint config with keys: name, url, timeout.
    """
    # Record the exact time before sending the request
    # so we can calculate how long the response takes
    start = time.time()
    try:
        # Send an async GET request — await yields control while waiting
        # so other endpoint checks can run concurrently during the wait
        resp = await client.get(
            endpoint["url"],
            timeout=endpoint["timeout"]
        )
        # Calculate total round-trip time in milliseconds
        elapsed = (time.time() - start) * 1000

        return {
            "name":        endpoint["name"],
            "url":         endpoint["url"],
            "status":      resp.status_code,
            "response_ms": round(elapsed, 2),
            # ok is True only for 200 — anything else is flagged
            "ok":          resp.status_code == 200
        }

    except Exception as e:
        # Request failed entirely — timeout, DNS failure, connection refused, etc.
        # We return a structured error dict so display_results() can handle it
        # without needing to know what type of error occurred.
        log.warning(f"Failed to reach {endpoint['name']}: {e}")
        return {
            "name":        endpoint["name"],
            "url":         endpoint["url"],
            "status":      "ERROR",
            "response_ms": None,
            "ok":          False
        }


async def run_checks(endpoints: list[dict]) -> list[dict]:
    """Run all endpoint checks concurrently and return a list of results."""
    # Create one shared AsyncClient for all requests.
    # async with ensures the connection pool is properly closed after all
    # checks complete — equivalent to a try/finally cleanup block.
    async with httpx.AsyncClient() as client:
        # asyncio.gather() runs all coroutines simultaneously.
        # The * unpacks the list comprehension into individual arguments
        # because gather() expects separate coroutines, not a list.
        results = await asyncio.gather(
            *[check_endpoint(client, ep) for ep in endpoints]
        )
        return results


def display_results(results: list[dict]) -> None:
    """Display health check results in a formatted terminal table."""
    # Build a rich Table — columns are defined once before the loop
    table = Table(title="API Health Monitor")

    # Each column has a fixed style applied to all its cells
    table.add_column("Name",          style="cyan")
    table.add_column("URL",           style="dim")
    table.add_column("Status",        style="bold")
    table.add_column("Response Time", style="yellow")
    table.add_column("Result")

    for r in results:
        # Use rich markup to color the result cell —
        # green for healthy endpoints, red for failures
        result_text = "[green]✓ UP[/green]" if r["ok"] else "[red]✗ DOWN[/red]"

        # Show N/A for response time when the request failed entirely
        response_time = f"{r['response_ms']}ms" if r["response_ms"] else "N/A"

        # add_row() requires all values to be strings
        table.add_row(
            r["name"],
            r["url"],
            str(r["status"]),
            response_time,
            result_text
        )

    # Render and print the completed table to the terminal
    console.print(table)


async def main() -> None:
    """Parse command-line arguments and run the health monitor."""
    # Create the CLI interface
    parser = argparse.ArgumentParser(
        description="API Health Monitor — check endpoint status and response times"
    )

    # Positional argument — path to the JSON config file containing endpoints
    parser.add_argument(
        "input",
        type=Path,
        help="Path to endpoints.json config file"
    )

    # Parse what the user typed in the terminal
    args = parser.parse_args()

    # Load endpoints from the JSON config file
    endpoints = load_endpoints(args.input)

    # Run all checks concurrently — await pauses here until all results are in
    results = await run_checks(endpoints)

    # Display the results table in the terminal
    display_results(results)


# ─── Guard ────────────────────────────────────────────────────────────────────
# asyncio.run() is required here instead of main() directly because main()
# is an async function. asyncio.run() creates the event loop, runs the
# coroutine, and shuts the loop down cleanly when done.
if __name__ == "__main__":
    asyncio.run(main())