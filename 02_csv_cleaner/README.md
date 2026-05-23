# 02 — CSV Data Cleaner & Reporter

A data quality tool that loads a CSV file, automatically detects and fixes common data problems, and outputs a clean file along with a summary report. Built around a real employee dataset with intentionally introduced data quality issues.

## Features

- Drops completely empty rows
- Removes duplicate records (ignoring ID columns)
- Standardizes inconsistent text casing across any column
- Flags invalid email formats using regex
- Flags invalid date formats using regex
- Handles whitespace-only cells that evade standard null checks
- Outputs a clean CSV file and a full terminal report

## Usage

```bash
# Install dependencies
pip install pandas

# Run the cleaner
python cleaner.py sample_data.csv clean_output.csv
```

## Data Quality Issues Detected

| Issue | Location | Action |
|-------|----------|--------|
| Completely empty row | E010 | Dropped |
| Duplicate records | E001/E004, E003/E017 | Dropped |
| Inconsistent status casing | E012, E023 | Fixed |
| Invalid email format | E008 | Flagged |
| Missing emails | E003, E017 | Flagged |
| Invalid date format | E019 | Flagged |
| Missing salary | E005, E022 | Reported |
| Missing phone | E006, E015 | Reported |

## The Professional Data Cleaning Process

1. **EDA** — explore the data before touching it
2. **Profile** — understand each column's expected vs actual values
3. **Document** — write down every issue before fixing anything
4. **Decide** — flag, fix, or drop each issue deliberately
5. **Pipeline** — write one function per issue

> **Golden Rule:** Never modify the original file. Always read from input, write to output.

## Concepts Covered

| Concept | Description |
|---------|-------------|
| `pandas` DataFrames | In-memory tabular data |
| `dropna()` | Removing empty rows |
| `drop_duplicates()` | Removing duplicate records |
| `str.match()` | Regex pattern matching on columns |
| `fillna()` | Safe handling of missing values |
| `replace()` with regex | Catching whitespace-only cells |
| Function chaining | Each function takes and returns a DataFrame |
| Debugging with `repr()` | Inspecting raw cell values |
