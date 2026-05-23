# 01 — Smart File Organizer

A command-line tool that automatically scans a directory and moves files into organized subfolders based on their file extension or modification date.

## Features

- Sorts files by type (Images, Documents, Code, Archives, Videos) or by year/month
- Collision-safe — renames duplicates instead of overwriting
- `--dry-run` mode previews every move without touching a single file
- Undo log — reverse any organize run with `--undo undo_log.json`
- Custom rules via JSON config file

## Usage

```bash
# Install dependencies (none required — standard library only)

# Basic — organize a folder in-place
python organizer.py ~/Downloads

# Preview only — no files moved
python organizer.py ~/Downloads --dry-run

# Sort to a separate destination
python organizer.py ~/Downloads -d ~/Sorted

# Sort by year/month instead of file type
python organizer.py ~/Downloads --sort-by date

# Use a custom rules file
python organizer.py ~/Downloads --config my_rules.json

# Undo the last run
python organizer.py --undo undo_log.json
```

## Custom Rules (`my_rules.json`)

```json
{
  ".sketch": "Design",
  ".fig":    "Design",
  ".sql":    "Database"
}
```

## Concepts Covered

| Concept | Description |
|---------|-------------|
| `pathlib.Path` | Modern file path handling |
| `shutil.move()` | Safe file moving |
| `argparse` | Full CLI interface with flags |
| `logging` | Timestamped structured output |
| Hash maps | O(1) extension lookups |
| Type hints | Throughout the codebase |
| Guard clauses | Early exit pattern |
| `if __name__ == "__main__"` | Entry point convention |
