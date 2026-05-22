"""
Smart File Organizer
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
"""

# ─── Standard library imports ─────────────────────────────────────────────────
# These come built into Python — no installation needed.
# We import only what we need, one per line (PEP 8 style guide).
import argparse   # builds our command-line interface (flags like --dry-run)
import logging    # structured messages instead of print() — timestamps + severity
import os         # low-level OS operations (we use this sparingly)
import shutil     # high-level file operations — move, copy, delete
from pathlib import Path  # modern way to work with file paths (replaces os.path)


# ─── Default rules dictionary ─────────────────────────────────────────────────
# This is the brain of the organizer.
# It maps every file extension (key) to a destination folder name (value).
#
# Why a dictionary and not a list?
# Because dictionaries use hash maps under the hood — looking up ".jpg" is
# instant (O(1)) no matter how many entries exist. A list would require
# scanning every entry one by one (O(n)) which slows down with scale.
#
# Why extensions as keys and folders as values (not the other way around)?
# Because at runtime we have the extension and need to find the folder.
# The lookup goes: ".jpg" → "Images", never "Images" → ".jpg".
#
# Type hint dict[str, str] tells any reader (and your IDE) exactly what
# this variable contains — keys are strings, values are strings.
DEFAULT_RULES: dict[str, str] = {
    # Images — common raster and vector formats
    ".jpg":  "Images",
    ".jpeg": "Images",
    ".png":  "Images",
    ".gif":  "Images",
    # Documents — text-based files meant to be read
    ".pdf":  "Documents",
    ".docx": "Documents",
    ".txt":  "Documents",
    ".md":   "Documents",
    # Code — source files across common languages
    ".py":   "Code",
    ".js":   "Code",
    ".html": "Code",
    ".css":  "Code",
    # Archives — compressed file containers
    ".zip":  "Archive",
    ".tar":  "Archive",
    ".gz":   "Archive",
    # Videos — common video container formats
    ".mp4":  "Videos",
    ".mov":  "Videos",
    ".mkv":  "Videos",
}


# ─── Logging configuration ────────────────────────────────────────────────────
# We configure logging once here at the top level, before any functions run.
#
# Why logging instead of print()?
# logging gives every message a timestamp, a severity level, and a source.
# When something breaks on file 312 out of 500, you'll know exactly when
# and where it happened. print() gives you none of that context.
#
# level=INFO means we show INFO, WARNING, ERROR, CRITICAL — but not DEBUG.
# DEBUG is for very detailed internal messages you only want during development.
#
# The format string controls what each line looks like:
#   %(asctime)s      → timestamp:   18:42:01
#   %(levelname)-8s  → severity:    INFO     (padded to 8 chars for alignment)
#   %(message)s      → our message: Moving photo.jpg → Images/
#
# datefmt controls the timestamp format — %H:%M:%S = hours:minutes:seconds
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)

# getLogger(__name__) creates a logger named after this module.
# __name__ is a special Python variable — when you run this file directly
# it equals "__main__". When imported by another script it equals the filename.
# This is the standard pattern in every professional Python codebase.
log = logging.getLogger(__name__)

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():#Loop through the folder
            continue          #Skip anything that is not a file
        ext = item.suffix.lower() #get the extension and lowercse it
        folder = rules.get(ext, "Misc") #look up which folder it belongs to
        destination = source/folder#Build the destination path
        destination.mkdir(parents=True, exist_ok=True)#create the folder if it does  not exist
        shutil.move(str(item), str(destination))#move the file
        log.info(f"Moved {item.name} -> {folder}/")#logs what happened

def main():
    #Creates the CLI interface
    parser = argparse.ArgumentParser(
        description="Smart File Organizer CLI"
        )
    #Defines the source as a positional argument
    parser.add_argument("source", type=Path)
    #Parses the arg
    args = parser.parse_args()
    organize(args.source, DEFAULT_RULES)

if __name__ == "__main__":
    main()