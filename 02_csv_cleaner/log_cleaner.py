"""
CSV Data Cleaner
================
Loads a CSV file, applies a series of cleaning rules, and writes a sanitized
version of the dataset to a new file.

Usage:
    python cleaner.py <input_file>

Example:
    python cleaner.py data.csv

Author : ivankoueniwork-19889
Script : 02 / 10
"""

import argparse
import logging
import pandas as pd
from pathlib import Path
import unicodedata


# ─── Logging configuration ────────────────────────────────────────────────────
# We configure logging once at the top level, before any functions run.
#
# Why logging instead of print()?
# logging gives every message a timestamp, a severity level, and a source.
# When something breaks on file 312 out of 500, you will know exactly when
# and where it happened. print() gives you none of that context.
#
# level=INFO means we show INFO, WARNING, ERROR, CRITICAL — but not DEBUG.
# DEBUG is for detailed internal messages you only want during development.
#
# Format string breakdown:
#   %(asctime)s      → timestamp   : 18:42:01
#   %(levelname)-8s  → severity    : INFO     (padded to 8 chars for alignment)
#   %(message)s      → our message : Removed 3 duplicate rows
#
# datefmt controls the timestamp format — %H:%M:%S = hours:minutes:seconds
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
# getLogger(__name__) creates a logger named after this module.
# __name__ equals "__main__" when run directly, or the filename when imported.
# This is the standard pattern used in every professional Python codebase.
log = logging.getLogger(__name__)


def load_csv(path: Path) -> pd.DataFrame:
    """Load a CSV file from disk and return it as a DataFrame."""
    #Log that we are loading the file
    log.info(f"loading file {path}")
    #Load the CSV
    df = pd.read_csv(path)
    #Log how many rows and columns were loaded
    log.info(f"{df.shape[0]} rows loaded and {df.shape[1]} columns loaded")
    return df


def drop_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows where every column is empty. Returns cleaned df."""
    #store the row count before dropping
    row_count = len(df)
    # strip whitespace from the entire DataFrame before dropping empty rows
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    #replace empty strings with NaN
    df = df.replace(r"^\s*$", pd.NA, regex=True)
    #drop empty rows
    df = df.dropna(how="all")
    #record how many rows were dropped
    new_row_count = len(df)
    row_count_dropped = row_count - new_row_count
    #Log how many were dropped
    log.info(f"Dropped {row_count_dropped} empty row(s)")
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove fully duplicate rows. Returns deduplicated df."""
    #Record how many rows exist before
    row_count = len(df)
    #Remove duplicate rows
    df = df.drop_duplicates()
    #record how many rows were dropped
    new_row_count = len(df)
    row_count_dropped = row_count - new_row_count
    #Log how many were dropped
    log.info(f"Dropped {row_count_dropped} duplicate row(s)")
    return df


def clean_text_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Convert every value in a given column to lowercase."""
    #Apply lowercase to the entire column and store it back
    df[column_name] = df[column_name].str.lower()
    #Log that the column was standardized
    log.info(f"The entire {column_name} column was standardized")
    return df

def normalize_url(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Normalize URL paths in a DataFrame column."""

    def clean_url(url: str) -> str:
        if not isinstance(url, str):
            return ""

        # Trim whitespace
        url = url.strip()

        # Normalize Unicode (handles weird characters safely)
        url = unicodedata.normalize("NFKC", url)

        # Lowercase for consistency
        url = url.lower()

        # Collapse multiple slashes
        while "//" in url:
            url = url.replace("//", "/")

        # Remove trailing slash unless it's the root
        if url != "/" and url.endswith("/"):
            url = url[:-1]

        return url

    df[column_name] = df[column_name].apply(clean_url)
    log.info(f"Normalized URL column: {column_name}")
    return df

VALID_METHODS = {"GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"}

def normalize_method(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Normalize HTTP methods in a DataFrame column."""

    def clean_method(method: str) -> str:
        if not isinstance(method, str):
            return "UNKNOWN"

        cleaned = method.strip().upper()

        if cleaned in VALID_METHODS:
            return cleaned

        return "UNKNOWN"

    df[column_name] = df[column_name].apply(clean_method)
    log.info(f"Normalized HTTP method column: {column_name}")
    return df


def flag_invalid_emails(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Flag invalid emails by adding an email_valid column (True/False)."""
    #Define the regex Pattern
    pattern = r"[^@]+@[^@]+\.[^@]+"
    #Apply it to email column
    df["email_valid"] = df[column_name].fillna("").str.match(pattern)
    #record how many invalid emails were found
    invalid_emails = (df["email_valid"] == False).sum()
    #Log how many emails were invalid
    log.info(f"There were {invalid_emails} invalid emails")
    return df

def flag_invalid_dates(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Flag invalid dates by adding a date_valid column (True/False)."""
    #Define the regex Pattern
    pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
    #Apply it to date column
    df["date_valid"] = df[column_name].fillna("").str.match(pattern)
    #record how many invalid dates were found
    invalid_dates = (df["date_valid"] == False).sum()
    #Log how many dates were invalid
    log.info(f"There were {invalid_dates} invalid dates")
    return df

def flag_invalid_status_codes(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Flag invalid HTTP status codes."""
    pattern = r"^(100|101|200|201|204|301|302|400|401|403|404|500|502|503)$"
    df["status_valid"] = df[column_name].astype(str).str.match(pattern)
    invalid = (~df["status_valid"]).sum()
    log.info(f"There were {invalid} invalid status codes")
    return df


def save_clean_csv(df: pd.DataFrame, output: Path) -> None:
    """Save the cleaned DataFrame to a CSV file on disk."""
    #Save the CSV to that path
    df.to_csv(output, index=False)
    #Log that the file was saved and where
    log.info(f"Clean file saved to {output}")

def generate_report(df: pd.DataFrame) -> None:
    """
    Generate and log a complete summary report of the cleaned DataFrame.
    Automatically adapts to whatever validation columns exist.
    """

    log.info("────────── CLEANING SUMMARY REPORT ──────────")

    # Basic shape
    log.info(f"Total rows remaining : {len(df)}")
    log.info(f"Total columns        : {len(df.columns)}")

    # Missing values
    missing = df.isnull().sum()
    log.info("Missing values per column:")
    for col, count in missing.items():
        log.info(f"  {col:<20} {count}")

    # Detect all *_valid columns automatically
    validation_columns = [c for c in df.columns if c.endswith("_valid")]

    if validation_columns:
        log.info("Validation summary:")
        for col in validation_columns:
            invalid_count = (~df[col]).sum()
            log.info(f"  {col:<20} {invalid_count} invalid")
    else:
        log.info("No validation columns found.")

    # URL normalization summary
    if "url" in df.columns:
        log.info(f"Unique normalized URLs: {df['url'].nunique()}")

    # Method normalization summary
    if "method" in df.columns:
        log.info(f"HTTP methods present  : {df['method'].unique().tolist()}")

    log.info("──────────── END OF REPORT ─────────────")


 


def main() -> None:
    """Parse command-line arguments and run the CSV cleaner."""
 
    # Create the CLI interface
    parser = argparse.ArgumentParser(
        description="CSV Data Cleaner"
    )
 
    # Define source as a positional argument
    # type=Path automatically converts the string input into a Path object
    parser.add_argument(
        "input",
        type=Path,
        help="Path to the directory the file is from"
    )
    
    # Define output as a positional argument
    # type=Path automatically converts the string input into a Path object
    parser.add_argument(
        "output",
        type=Path,
        help="Path to the directory the clean csv will be saved"
    )
 
    # Parse what the user typed in the terminal
    args = parser.parse_args()
    
    df = load_csv(args.input)
    df = drop_empty_rows(df)
    df = drop_duplicates(df)
    df = clean_text_column(df,"url")
    df = normalize_url(df,"url")
    df = normalize_method(df, "method")
    df = flag_invalid_status_codes(df,"status")
    df = flag_invalid_dates(df,"timestamp")
    save_clean_csv(df, args.output)
    generate_report(df)


# ─── Guard ────────────────────────────────────────────────────────────────────
# This block only runs when the script is executed directly.
# If another script imports this file, main() will NOT run automatically.
# This is a universal Python convention — always include it.
if __name__ == "__main__":
    main()
 
