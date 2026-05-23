"""
Email Digest Generator
======================
Collects data from one or more sources, formats it into a structured summary,
and sends a consolidated email digest to a target recipient list. This script
is designed for automation workflows where daily, hourly, or event‑driven
summaries need to be delivered without manual intervention.

Usage:
    python digest.py <csv_file>

Example:
    python digest.py sample_data.csv

Author : ivankoueniwork-19889
Script : 03 / 10
"""

# standard library
import argparse
from datetime import datetime
from email.mime.text import MIMEText
import logging
import os
from pathlib import Path
import smtplib


# third party
from dotenv import load_dotenv
import pandas as pd


# ─── Logging configuration ────────────────────────────────────────────────────
# We configure logging once at the top level, before any functions run.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)

# getLogger(__name__) creates a logger named after this module.
# __name__ equals "__main__" when run directly, or the filename when imported.
# This is the standard pattern used in every professional Python codebase.
log = logging.getLogger(__name__)
load_dotenv()


def load_credentials() -> tuple[str, str]:
    """Load email credentials from environment variables."""
    sender = os.getenv("EMAIL_SENDER")
    if not sender:
        raise ValueError("Email sender missing")
    receiver = os.getenv("EMAIL_RECEIVER")
    if not receiver:
        raise ValueError("Email receiver missing")
    log.info("credentials were loaded successfully")
    return sender, receiver


def build_summary(path: Path) -> str:
    """Build a clean, formatted summary string for the email digest."""

    log.info(f"Loading file {path}")
    df = pd.read_csv(path)

    total_employees = len(df)
    total_departments = df["department"].nunique()
    avg_salary = df["salary"].mean()
    missing_values = df.isnull().sum().sum()

    return f"""
Daily Employee Digest
=====================

Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}

Summary:
    • Total employees:               {total_employees}
    • Number of departments:         {total_departments}
    • Average salary:                ${avg_salary:,.2f}
    • Total missing values:          {missing_values}

This is an automated summary generated from the latest dataset.
"""


def send_email(sender: str, receiver: str, body: str) -> None:
    """Send email digest via Gmail SMTP with TLS."""
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(body)
    msg["Subject"] = "Daily Employee Digest"
    msg["From"]    = sender
    msg["To"]      = receiver

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg.as_string())
        log.info("Email sent successfully")
    except Exception as e:
        log.error(f"Failed to send email: {e}")


def main() -> None:
    """Parse command-line arguments and run email sender."""
 
    # Create the CLI interface
    parser = argparse.ArgumentParser(
        description="Email Digest"
    )
 
    # Define source as a positional argument
    # type=Path automatically converts the string input into a Path object
    parser.add_argument(
        "input",
        type=Path,
        help="Path to the directory the file is from"
    )
    # Parse what the user typed in the terminal
    args = parser.parse_args()
    sender, receiver = load_credentials()
    content = build_summary(args.input)
    send_email(sender, receiver, content)

# ─── Guard ────────────────────────────────────────────────────────────────────
# This block only runs when the script is executed directly.
# If another script imports this file, main() will NOT run automatically.
# This is a universal Python convention — always include it.
if __name__ == "__main__":
    main()
    