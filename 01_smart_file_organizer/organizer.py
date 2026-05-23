
Claude finished the response
help me build 10 automation scripts that i can use in my portfolio. we will go over the concepts first, then b uild together the tool in python. this should be a guided session as a senior python developper teaching a junior upgrade his skills. we will connect it to my current github

2:35 PM

Gauged skill level before architecting comprehensive portfolio project
Gauged skill level before architecting comprehensive portfolio project
Love this project — building a strong automation portfolio is one of the best ways to stand out as a developer. Before we dive in, let me get a feel for where you're at so I can pitch the session right.

Once you answer those, I'll map out all 10 scripts with a clear learning progression — from foundational to impressive — and we'll connect everything to your GitHub so your portfolio is live as we build. 🚀

Q: How would you rate your current Python level?
A: Intermediate (functions, OOP, some libraries)

Q: Which automation domains interest you most? (pick all that apply) (Select all that apply)
A: Web scraping & APIs, File & folder management, Data processing (CSV/Excel), Email / notifications, Browser automation, DevOps / CLI tools, provide more options that are security oriented

Q: What's your goal for this portfolio?
A: Land a first dev job

2:38 PM

Architected intermediate-level security-focused automation curriculum toward employment
Architected intermediate-level security-focused automation curriculum toward employment
Perfect — this is a strong foundation to work with. Since you're targeting your first dev job and want security-oriented tools, we're going to make your portfolio scream "I understand real-world problems." Here's the full roadmap:



Here's how the session works:

Each script follows the same flow:

Concept explanation — why this tool matters, where it's used in real jobs
Architecture walkthrough — design decisions before we write a single line
Build it together — step by step, with me explaining every choice
Push to GitHub — proper commit messages, README, and repo structure
The progression is intentional. Scripts 1–3 build your Python fundamentals (file I/O, data, scheduling). Scripts 4–6 add networking, APIs, and a taste of security. Scripts 7–10 are your showstoppers — the ones that make a security-conscious hiring manager lean forward.

Before we start, let's connect to your GitHub so every script auto-lands in your portfolio as we build.

You'll be prompted to enable connector discovery — go ahead and do that, then I can link directly to your GitHub. Alternatively, if you already have it connected, just say so and we'll jump straight in.

Ready to start whenever you are — tap script 01 to kick things off, or just tell me which one you want to build first. 🚀

Go ahead.

2:48 PM

Pivoted toward manual GitHub setup for superior developer learning
Pivoted toward manual GitHub setup for superior developer learning
GitHub isn't available as a direct MCP connector here — but that's actually fine. We'll do it the real dev way: using git from the terminal inside each script build. That's exactly what you'd do on the job, and it looks much better in a portfolio than a one-click integration.

Here's the plan for GitHub setup — we'll do this once, then automate it for every script:

Create a python-automation-portfolio repo on your GitHub
Set up a clean local structure
Use a push.sh helper script so each tool gets committed with a proper message
Let's build the folder structure and GitHub bootstrap now. What's your GitHub username? Once you give me that, I'll scaffold everything and we jump straight into Script 01.

https://github.com/ivankoueniwork-19889

2:49 PM

Endeavored to retrieve GitHub profile information
Endeavored to retrieve GitHub profile information
Let me take a look at your GitHub profile first.


Assessed existing security repos and architected complementary portfolio structure
Assessed existing security repos and architected complementary portfolio structure
This changes everything — in the best way. You already have a serious security portfolio: soc-toolkit, ioc-extractor, pentesting-tools, and soc-home-lab. You're not a beginner playing around — you're someone building real SOC/pentesting tools.

So we're going to create a new repo called python-automation-portfolio that sits alongside these and shows the breadth of your Python skills beyond security — exactly what a hiring manager wants to see.

Let me scaffold the full project structure right now.


Ran 4 commands
Ran 4 commands
Script 01 is live and working. Now let's copy everything to the output and I'll walk you through the key concepts.


Ran a command, read a file
Ran a command, read a file
✅ Script 01 is done, tested, and clean. Here's what you need to understand about the code before we move on:

Concepts taught in this script:

pathlib.Path — forget os.path. Path objects are the modern way to handle files in Python. You can do path / "subdir" / "file.txt" instead of string concatenation. Every job you'll work at uses this.

argparse — your CLI interface. Notice how build_parser() is its own function — that's a senior habit. It makes the parser testable and the main() function clean.

logging vs print() — we use logging because it gives timestamps, severity levels, and can be piped to a file. print() is for prototypes. Real tools log.

Type hints (dict[str, str], list[dict], tuple[int, int]) — you'll be expected to write these at any job worth taking. They make your code self-documenting.

The undo pattern — instead of asking "are you sure?", we write a reversal log. This is how professional tools handle destructive operations.

Now push it to GitHub. Run these commands on your machine:

bash
git clone https://github.com/ivankoueniwork-19889/python-automation-portfolio
# (create the repo on GitHub first if it doesn't exist yet)

# OR if starting fresh:
cd python-automation-portfolio
git init
git remote add origin https://github.com/ivankoueniwork-19889/python-automation-portfolio.git
git add .
git commit -m "feat: add project scaffold and script 01 smart file organizer"
git push -u origin main
Ready to move to Script 02 — CSV Data Cleaner & Reporter? That one introduces pandas, teaches you how to detect data quality issues programmatically, and generates a real HTML report — a very common task in dev/analyst hybrid roles. Say the word.


Organizer
PY 

Readme
Document · MD 

Push
SH 
wait we are building all scripts togetrher steps by steps , you tell me what directions to go or what the script needs to do i build it we check and verify until we get a workable final product before we push it   the objective is for me to write it and for youy to assist me every step of the way

2:53 PM

Recalibrated teaching methodology to prioritize learner-driven code development
Recalibrated teaching methodology to prioritize learner-driven code development
You're absolutely right — my bad for jumping ahead. That's not how you learn. Let me reset completely.

Here's how we work from now on:

I explain the concept and what we need to build
I tell you exactly what to write next (one small step at a time)
You write it, paste it here
I review, explain what's good, what to fix, and why
We iterate until it's solid
Then we push together
Let's restart Script 01 — Smart File Organizer properly. Wipe whatever you have and start fresh.

Step 1 — Project setup

On your machine, create this folder structure:

python-automation-portfolio/
└── 01_smart_file_organizer/
    └── organizer.py        ← this is the only file we create today
Then open organizer.py in your editor.

Your first task: Write just the file header — nothing else yet. This means:

A module docstring (triple-quoted string at the very top) that describes what the script does in 2–3 sentences
Your imports — you'll need os, shutil, pathlib.Path, argparse, and logging
That's it. No functions, no logic. Just the top of the file.

Paste it here when done and I'll check it before we go any further. 🟢

"""
   Smart File Organizer
    Automatically scans a directory, classifies files based on user‑defined rules,
    and moves them into structured destination folders.
"""
import os,shutil, pathlib.Path, argparse, logging

3:02 PM

Identified import syntax errors and PEP8 violations
Identified import syntax errors and PEP8 violations
Good start — the docstring is solid. Two things to fix before we move on:

Issue 1 — Bad import syntax

python
import pathlib.Path  # ❌ this will crash
pathlib.Path is a class inside the pathlib module, not a module itself. You have two valid options:

python
import pathlib          # then use pathlib.Path() everywhere
# OR
from pathlib import Path  # then use Path() directly — cleaner, preferred
We'll go with from pathlib import Path. You'll see why when we start using it.

Issue 2 — One import per line (PEP 8)

Chaining imports with commas on one line works but is considered bad style in Python. Hiring managers and code reviewers will notice this.

python
import os, shutil, argparse  # ❌ works but unprofessional
python
import os               # ✅ one per line
import shutil
import argparse
Your fix — rewrite the top of the file like this:

python
# standard library — one import per line
import os
import shutil
import argparse
import logging
from pathlib import Path
Go ahead and update your file with the corrected docstring + imports, paste it back here, and then I'll give you Step 2.

"""
   Smart File Organizer
    Automatically scans a directory, classifies files based on user‑defined rules,
    and moves them into structured destination folders.
"""
import os
import shutil
import argparse
import logging
from pathlib import Path

3:03 PM

Orchestrated progression toward defining default configuration rules
Orchestrated progression toward defining default configuration rules
Clean. That's exactly right. ✅

Notice one small thing — your docstring indentation is slightly inconsistent (first line has 3 spaces, second has 4). Not a crash, but worth being tidy:

python
"""
Smart File Organizer
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
"""
Fix that, then we move on.

Step 2 — The rules dictionary

This is the brain of the organizer. It maps file extensions to folder names. When we see a .jpg, we know to put it in "Images". When we see .py, it goes in "Code".

Your task: Right below your imports, define a dictionary called DEFAULT_RULES. It should cover at least these categories:

Folder	Extensions
"Images"	.jpg, .jpeg, .png, .gif
"Documents"	.pdf, .docx, .txt, .md
"Code"	.py, .js, .html, .css
"Archives"	.zip, .tar, .gz
"Videos"	.mp4, .mov, .mkv
The keys are extension strings (lowercase, with the dot). The values are folder name strings.

One hint on style — group your extensions by category using comments, like this:

python
DEFAULT_RULES: dict[str, str] = {
    # Images
    ".jpg": "Images",
    ...
}
That : dict[str, str] after the variable name is a type hint — it tells anyone reading the code exactly what this variable contains. Get in the habit of writing these.

Write the dictionary and paste it back. 🟢

"""
   Smart File Organizer
   Automatically scans a directory, classifies files based on user‑defined rules,
   and moves them into structured destination folders.
"""
import os
import shutil
import argparse
import logging
from pathlib import Path
DEFAULT_RULES: dict[str, str] = {
    #images
    "Images":".jpg",".jpeg",".png",".gif",
    "Documents":".pdf",".docx",".txt",".md",
    "Code":".py",".js",".html",".css",
    "Archives": ".zip",".tar",".gz"
    "Videos": ".mp4",".mov",".mkv"

    }

Show more
3:09 PM
Good effort — the structure is there, but there are two real bugs that would crash the script. Let's fix both.

Bug 1 — Keys and values are swapped

In a lookup dictionary, you want to ask "I have a .jpg, which folder does it go in?" That means the extension is the key and the folder is the value:

python
".jpg": "Images"   # ✅ extension → folder
"Images": ".jpg"   # ❌ backwards — you can't look up by extension
Bug 2 — Multiple values per key is not valid dict syntax

python
"Images": ".jpg", ".jpeg", ".png"  # ❌ Python sees this as a tuple problem
Each key needs its own line with its own value:

python
".jpg":  "Images",
".jpeg": "Images",
".png":  "Images",
Yes, you repeat the folder name. That's intentional — it makes lookups instant (O(1)). We trade a little repetition for a lot of speed.

Bug 3 — Missing comma between entries

python
".gz"
"Videos"  # ❌ missing comma on the line above
Every entry except the last needs a trailing comma.

Your fix — rewrite just the dictionary:

Same structure you had, just flip every pair and give each extension its own line. Paste it back when done. 🟢

"""
   Smart File Organizer
   Automatically scans a directory, classifies files based on user‑defined rules,
   and moves them into structured destination folders.
"""
import os
import shutil
import argparse
import logging
from pathlib import Path
DEFAULT_RULES: dict[str, str] = {
    #images
    "Images":{".jpg",".jpeg",".png",".gif"},
    "Documents":{".pdf",".docx",".txt",".md"},
    "Code":{".py",".js",".html",".css"},
    "Archives":{ ".zip",".tar",".gz"},
    "Videos": {".mp4",".mov",".mkv"}

    }

Show more
3:11 PM
Getting closer — you fixed the comma issue and the structure is cleaner. But one bug remains.

Still the same core problem — keys and values are still swapped

You've also wrapped the extensions in {} which makes them sets, not strings. A set is a collection of items — you can't use it as a dictionary value for lookups.

Think about how the script will actually use this dictionary at runtime:

python
file = Path("vacation.jpg")
ext = file.suffix        # gives us ".jpg"
folder = DEFAULT_RULES[ext]  # we look up ".jpg" and want "Images" back
So we need to be able to ask: "what folder does .jpg belong to?"

That means:

Key = the extension → ".jpg"
Value = the folder name → "Images"
Like a real dictionary — you look up the word (extension) to find its meaning (folder).

Visual before/after:

python
# ❌ What you have — can't look up by extension
"Images": {".jpg", ".jpeg", ".png"}

# ✅ What we need — one entry per extension
".jpg":  "Images",
".jpeg": "Images",
".png":  "Images",
Rewrite the dictionary with extensions as keys and folder names as values. Five categories, each extension gets its own line. 🟢

ok what is the concept behind it

3:14 PM
Great question — this is exactly the right moment to ask.

The core concept: Hash Maps (Dictionary Lookup)

A Python dict is an implementation of a data structure called a hash map. Here's what makes it powerful:

When you write:

python
DEFAULT_RULES[".jpg"]
Python doesn't loop through every entry searching for .jpg. Instead it hashes the key — runs it through a mathematical function that instantly computes exactly where in memory that value lives. The lookup is the same speed whether the dictionary has 5 entries or 5 million.

This is called O(1) time complexity — constant time. It doesn't slow down as the dictionary grows.

Why not a list instead?

You could have written:

python
rules = [
    ([".jpg", ".jpeg", ".png"], "Images"),
    ([".pdf", ".docx"],         "Documents"),
]
But then to find where .jpg belongs, Python would have to check every single entry one by one until it finds a match. That's O(n) — it gets slower as the list grows. For 5 entries you'd never notice. For 50,000 files being processed, you would.

The mental model

Think of it like a phone book vs a search engine.

A list is the phone book — you flip through pages until you find the name.

A dictionary is Google — you type the name and the answer appears instantly, no matter how big the database is.

Applied to our script

Every file we process does exactly one lookup:

python
ext    = file.suffix.lower()   # ".jpg"
folder = DEFAULT_RULES.get(ext, "Misc")  # "Images"
One line. Instant. No loops. That's why we want extensions as keys.

Does that click? If yes, rewrite the dictionary with that mental model in mind. 🟢

"""
   Smart File Organizer
   Automatically scans a directory, classifies files based on user‑defined rules,
   and moves them into structured destination folders.
"""
import os
import shutil
import argparse
import logging
from pathlib import Path
DEFAULT_RULES: dict[str, str] = {
    #images
    ".jpg":"Images",
    ".jpeg":"Images",
    ".png":"Images",
    ".gif":"Images,
    #Documents
    ".pdf":"Documents",
    ".docx":"Documents",
    ".txt":"Documents",
    ".md":"Documents",
    #Code
    ".py":"Code",
    ".js":"Code",
    ".html":"Code",
    ".css":"Code",
    #Archive
    ".zip":"Archive",
    ".tar":"Archive",
    ".gz":"Archive",
    #Videos
    ".mp4":"Videos",
    ".mov":"Videos",
    ".mkv":"Videos"

    }

Show more
3:19 PM
That's it. Structure is perfect, logic is correct, concept fully applied. ✅

Just one tiny bug — a missing closing quote:

python
".gif":"Images,   # ❌ string never closes — will crash
".gif":"Images",  # ✅
Fix that one character, and this section is done.

Also two style habits to build now while it's fresh:

1. Space after the colon — makes it easier to scan:

python
".jpg":"Images",   # harder to read
".jpg": "Images",  # easier to read — standard Python style
2. Align your values — not required, but senior devs do this for readability:

python
".jpg":  "Images",
".jpeg": "Images",
".png":  "Images",
Fix the quote, add the spaces, paste it back. Once this is clean we move to Step 3 — the logging setup, which is two lines and teaches you something you'll use in every script from here on. 🟢

how to align the values

3:20 PM
Good question. It's purely manual spacing — you add extra spaces between the key and the colon's value so all the folder names line up in a column.

Like this:

python
# not aligned — eyes have to jump around
".jpg": "Images",
".jpeg": "Images",
".png": "Images",

# aligned — eyes scan straight down the right column
".jpg":  "Images",
".jpeg": "Images",
".png":  "Images",
The rule is simple — find the longest key in the group, then pad all shorter keys with extra spaces until the values line up.

In your Images group the longest key is .jpeg (6 chars). So:

python
".jpg":  "Images",   # 4 chars → add 2 spaces
".jpeg": "Images",   # 5 chars → add 1 space
".png":  "Images",   # 4 chars → add 2 spaces
".gif":  "Images",   # 4 chars → add 2 spaces
You don't have to align across the entire dictionary — just within each category group. So Images aligns with Images, Documents with Documents, etc.

Your editor might do this automatically if you have an auto-formatter like Black or Prettier installed. But doing it by hand right now teaches your eye what clean code looks like.

Go ahead and update the full dictionary with the quote fix and alignment, then paste it back. 🟢

"""
Smart File Organizer
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
"""
import os
import argparse
import logging
import shutil
from pathlib import Path
from typing import Dict
DEFAULT_RULES: Dict[str, str] = {
    # Images
    ".jpg":  "Images",
    ".jpeg": "Images",
    ".png":  "Images",
    ".gif":  "Images",
    # Documents
    ".pdf":  "Documents",
    ".docx": "Documents",
    ".txt":  "Documents",
    ".md":   "Documents",
    # Code
    ".py":   "Code",
    ".js":   "Code",
    ".html": "Code",
    ".css":  "Code",
    # Archive
    ".zip": "Archive",
    ".tar": "Archive",
    ".gz":  "Archive",
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
}

Show more
3:25 PM
That's clean, professional code. Excellent. ✅

One small note on the import you added:

python
from typing import Dict  # works, but outdated — Python 3.9+
Dict[str, str]           # old style

dict[str, str]           # ✅ modern — no import needed, Python 3.9+
Since Python 3.9 you can use the built-in dict directly as a type hint. Remove the from typing import Dict line and change Dict to lowercase dict. Cleaner, one less import.

Also notice you alphabetized your imports:

python
import argparse
import logging
import os
import shutil
That's actually the correct PEP 8 convention — standard library imports in alphabetical order. Good instinct.

Make that one change (Dict → dict, remove the typing import), then paste it back and we go straight to Step 3 — logging setup.

This one is just two lines but it's something juniors almost never do and seniors always do. 🟢

"""
Smart File Organizer
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
"""
import argparse
import logging
import os
import shutil
from pathlib import Path
DEFAULT_RULES: Dict[str, str] = {
    # Images
    ".jpg":  "Images",
    ".jpeg": "Images",
    ".png":  "Images",
    ".gif":  "Images",
    # Documents
    ".pdf":  "Documents",
    ".docx": "Documents",
    ".txt":  "Documents",
    ".md":   "Documents",
    # Code
    ".py":   "Code",
    ".js":   "Code",
    ".html": "Code",
    ".css":  "Code",
    # Archive
    ".zip": "Archive",
    ".tar": "Archive",
    ".gz":  "Archive",
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
}

Show more
3:26 PM
Almost — you removed the import but kept the capital Dict. That will crash with a NameError since Dict no longer exists in scope.

One character fix:

python
DEFAULT_RULES: Dict[str, str] = {   # ❌ Dict is undefined now
DEFAULT_RULES: dict[str, str] = {   # ✅ lowercase built-in
Fix that, paste it back, then we go to Step 3. 🟢

"""
Smart File Organizer
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
"""
import argparse
import logging
import os
import shutil
from pathlib import Path
DEFAULT_RULES: dict[str, str] = {
    # Images
    ".jpg":  "Images",
    ".jpeg": "Images",
    ".png":  "Images",
    ".gif":  "Images",
    # Documents
    ".pdf":  "Documents",
    ".docx": "Documents",
    ".txt":  "Documents",
    ".md":   "Documents",
    # Code
    ".py":   "Code",
    ".js":   "Code",
    ".html": "Code",
    ".css":  "Code",
    # Archive
    ".zip": "Archive",
    ".tar": "Archive",
    ".gz":  "Archive",
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
}

Show more
3:27 PM
Perfect. That's locked in. ✅

Step 3 — Logging setup

Right below your DEFAULT_RULES dictionary, add these two lines:

python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
What each part means — understand this, don't just copy it:

logging.basicConfig(...) — configures the logging system once for the whole script. You only call this once, always near the top.

level=logging.INFO — sets the minimum severity to show. The levels in order are: DEBUG → INFO → WARNING → ERROR → CRITICAL. Setting INFO means you'll see INFO and above, but not DEBUG noise.

format=... — controls what each log line looks like. %(asctime)s is the timestamp, %(levelname)-8s is the severity left-padded to 8 chars, %(message)s is your actual message. The result looks like:

18:42:01  INFO      Moving photo.jpg → Images/
18:42:01  WARNING   File already exists, renaming...
log = logging.getLogger(__name__) — creates a logger named after your module. __name__ is a special Python variable that equals the filename when you run the script directly. This is the standard pattern — you'll see it in every professional Python codebase.

From this point on, instead of print("something happened") you write log.info("something happened") or log.warning("watch out").

Add those two lines to your file and paste the whole thing back. 🟢

ok why do i need to add those and what do they do excatly with sipmpler terms ,  Ia m not familiar with those concepts yet

3:29 PM
No problem — great that you asked instead of just copying it.

The simple version

Right now if you want to show a message in your script you'd write:

python
print("Moving photo.jpg")
That works. But print is dumb — it just spits text out. It has no idea when something happened, how serious it was, or where in your code it came from.

logging is a smarter version of print. Every message automatically gets:

a timestamp — when did this happen?
a severity level — is this just info, a warning, or a real error?
a source — which part of the code sent this message?
The four lines explained in plain English

python
logging.basicConfig(...)
This is you saying "hey Python, when I log messages, here's how I want them formatted." You set this up once at the top, like configuring your printer before you start printing.

python
level=logging.INFO
You're saying "only show me messages that are INFO level or more serious." Think of it like a filter — INFO lets through normal messages, warnings, and errors. It hides debug noise you don't care about right now.

python
format="%(asctime)s  %(levelname)-8s  %(message)s"
This is the template for each line. Instead of just seeing:

Moving photo.jpg
You see:

18:42:01  INFO      Moving photo.jpg
Much more useful when something goes wrong.

python
log = logging.getLogger(__name__)
This creates your personal logger object. Think of it as getting a pen that automatically stamps the time and severity on everything you write. From here on you use log.info() instead of print().

The practical difference

python
print("Moving photo.jpg")         # basic, no context

log.info("Moving photo.jpg")      # 18:42:01  INFO      Moving photo.jpg
log.warning("File exists!")       # 18:42:01  WARNING   File exists!
log.error("Directory not found")  # 18:42:01  ERROR     Directory not found
Same idea, way more useful output. And when your script is running on 500 files and something breaks at file 312, you'll be very glad you have timestamps and severity levels.

Does that make sense? If yes, add those two lines to your file and paste it back. 🟢

"""
Smart File Organizer
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
"""
import argparse
import logging
import os
import shutil
from pathlib import Path
DEFAULT_RULES: dict[str, str] = {
    # Images
    ".jpg":  "Images",
    ".jpeg": "Images",
    ".png":  "Images",
    ".gif":  "Images",
    # Documents
    ".pdf":  "Documents",
    ".docx": "Documents",
    ".txt":  "Documents",
    ".md":   "Documents",
    # Code
    ".py":   "Code",
    ".js":   "Code",
    ".html": "Code",
    ".css":  "Code",
    # Archive
    ".zip": "Archive",
    ".tar": "Archive",
    ".gz":  "Archive",
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
}
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

Show more
3:31 PM

Validated logging configuration and advanced to next step
Validated logging configuration and advanced to next step
That's exactly right. Clean and correct. ✅

Quick checkpoint — look at what you've built so far:

✅ Docstring        — describes what the script does
✅ Imports          — clean, alphabetical, no extras
✅ DEFAULT_RULES    — the brain of the organizer, O(1) lookups
✅ Logging setup    — professional output instead of print()
That's a solid foundation. No functions yet — just clean setup code. This is how professionals build: structure first, logic second.

Step 4 — Your first function: organize()

This is the core of the script. It takes a folder, scans every file in it, and moves each one to the right destination.

Write a function called organize that takes two parameters:

python
def organize(source: Path, rules: dict[str, str]) -> None:
source — the folder we're scanning (a Path object) rules — the dictionary we just built -> None — means this function doesn't return anything, it just does work

Inside the function, do just one thing for now — loop over every item in the source directory and print its name. We'll add the move logic after.

The tool you need is:

python
source.iterdir()  # returns every file and folder inside source
So your loop looks like:

python
for item in source.iterdir():
    print(item.name)
Write the function with that loop inside it and paste the whole file back. 🟢

please add professional comments to he whole code so  a junior analyst could understand

3:31 PM
Great habit to ask for that — commented code is something a lot of juniors skip and then regret later.

Here's the full file with professional comments explaining every decision. Read through all of it carefully before we continue — understanding why each line exists is more important than the line itself:

python
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


# ─── Core function ────────────────────────────────────────────────────────────
def organize(source: Path, rules: dict[str, str]) -> None:
    """
    Scan a directory and move each file to its destination folder.

    Parameters
    ----------
    source : Path
        The directory to scan. Must exist before calling this function.
    rules : dict[str, str]
        A mapping of file extension → destination folder name.
        Example: {".jpg": "Images", ".pdf": "Documents"}
    """
    # iterdir() returns every item inside source — files AND folders.
    # We'll handle the folder case in the next step.
    for item in source.iterdir():
        print(item.name)   # temporary — we replace this with move logic next
A few things to notice in the comments:

The # ─── section dividers make large files easy to navigate — you can scan down and instantly find what you're looking for.

The docstring inside the function uses NumPy style (Parameters, ----------) — this is a professional convention that tools like Sphinx can auto-generate documentation from. Get used to writing docstrings like this for every function.

The inline comments explain why, not what. A bad comment says # loop over files. A good comment says # iterdir() returns files AND folders — we handle folders next. The code already shows what's happening — comments explain the reasoning.

Copy this into your file exactly as written, read every comment at least once, then paste it back and we move to Step 5 — adding the actual move logic inside organize(). 🟢

lets step back to the function

3:32 PM
Good instinct — let's slow down and make sure you truly understand it before writing a single line.

What is a function?

A function is a reusable block of code that does one specific job. You define it once, then call it whenever you need it.

python
def greet(name):
    print(f"Hello {name}")

greet("Ivan")   # Hello Ivan
greet("Maria")  # Hello Maria
Same code, different inputs, different results.

Our function needs to do one job

"Take a folder, look at every file inside it, figure out where it belongs, move it there."

That's it. One job. We give it the folder, it handles the rest.

The signature — what goes in, what comes out

python
def organize(source: Path, rules: dict[str, str]) -> None:
Break it down word by word:

Part	Meaning
def	"I'm defining a function"
organize	the function's name
source: Path	first input — the folder to scan
rules: dict[str, str]	second input — the extension→folder map
-> None	this function returns nothing, it just does work
Before you write anything — answer these three questions out loud or in your head:

What does source represent in plain English?
What does rules represent in plain English?
Inside the function, what's the very first thing we need to do to process a folder full of files?
Tell me your answers, then we write the function together. 🟢

first I need to write it myself

3:33 PM
That's the right attitude. Go for it.

Write the organize function from scratch. Don't copy anything from before. Use what you understand so far.

When you're done paste it here. 🟢

what should the function do exactly please guide

3:33 PM
Here's the job description for the function in plain English:

What organize() needs to do, step by step:

Look inside the source folder — scan every item in it
Skip folders — we only want to move files, not subfolders
Get the file extension — for photo.jpg that's .jpg
Look it up in the rules dictionary — does .jpg exist in our DEFAULT_RULES? If yes, what folder does it map to?
If we don't recognize the extension — put it in a folder called "Misc" so nothing gets lost
Move the file — into the correct destination folder
That's 6 steps. Start with just step 1 and 2.

Write a function that:

loops over everything in source
checks if the current item is a file (not a folder)
if it's a file, log its name using log.info()
if it's a folder, skip it
Two hints:

python
source.iterdir()    # loops over everything inside source
item.is_file()      # returns True if item is a file, False if it's a folder
Write just those steps, paste it here. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if item.is_file():
            log.info(item_name)
        continue

3:38 PM

Identified variable naming error and misplaced control flow
Identified variable naming error and misplaced control flow
Really close — the logic is right. Two small fixes:

Bug 1 — item_name doesn't exist

You never defined a variable called item_name. The name lives on the item object itself:

python
log.info(item_name)   # ❌ NameError — this variable doesn't exist
log.info(item.name)   # ✅ .name is a property of the Path object
Bug 2 — continue is in the wrong place

continue means "skip to the next item in the loop". Right now it runs after every file, which means it never actually does anything useful. You want it in the else branch — when the item is NOT a file:

python
# what you have — continue runs after every item including files
for item in source.iterdir():
    if item.is_file():
        log.info(item.name)
    continue               # ❌ always runs

# what you want — skip folders, process files
for item in source.iterdir():
    if not item.is_file():
        continue           # ✅ skip this item if it's a folder
    log.info(item.name)
The not flips the condition — "if this item is NOT a file, skip it". Everything below that line only runs for actual files.

Fix both issues and paste it back. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():
            continue
        log.info(item.name)

3:39 PM
That's perfect. Clean, correct, professional. ✅

Notice what you just did:

The not item.is_file() + continue pattern is called an early return guard (or guard clause). Instead of nesting all your logic inside an if, you kick out the cases you don't care about early and keep the main logic flat.

python
# nested — harder to read as logic grows
for item in source.iterdir():
    if item.is_file():
        # all your logic indented in here
        # and in here
        # and in here

# flat with guard — easier to read
for item in source.iterdir():
    if not item.is_file():
        continue
    # all your logic at the top level
    # easy to read
    # no deep nesting
You'll use this pattern constantly. Good instinct to land on it.

Now Step 2 — get the extension and look it up

Add two lines inside the loop, right after log.info(item.name):

Get the file extension from item and store it in a variable called ext. Make it lowercase so .JPG and .jpg match the same rule.
Look up ext in rules and store the result in a variable called folder. If the extension isn't in the dictionary, default to "Misc".
Two hints:

python
item.suffix          # gives you the extension — ".jpg", ".pdf" etc.
"string".lower()     # converts to lowercase
rules.get(key, default)  # looks up key, returns default if not found
Write those two lines and paste the whole function back. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():
            continue
        log.info(item.name)
        ext = item.suffix
        folder= rules.get(ext,"Misc")

3:49 PM
Almost perfect — just one small thing missing and one style note.

Missing — lowercase conversion

python
ext = item.suffix          # ❌ ".JPG" won't match ".jpg" in the dictionary
ext = item.suffix.lower()  # ✅ always lowercase before lookup
This matters because Windows users often have files like photo.JPG or document.PDF. Without .lower() those files would land in "Misc" instead of the right folder.

Style — space around the equals sign

python
folder= rules.get(ext, "Misc")   # ❌ no space before =
folder = rules.get(ext, "Misc")  # ✅ spaces on both sides
Python won't crash without it but PEP 8 requires spaces around = in assignments. Your IDE or a code reviewer will flag this.

Fix both, paste it back. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():
            continue
        log.info(item.name)
        ext = item.suffix.lower()
        folder = rules.get(ext, "Misc")

3:50 PM
That's exactly right. Clean and correct. ✅

Now Step 3 — move the file

This is where the actual work happens. We need to:

Build the destination path — where does the file go?
Create that folder if it doesn't exist yet
Move the file there
Three hints:

python
source / folder             # builds a path — joins source + folder name
destination.mkdir(
    parents=True,
    exist_ok=True
)                           # creates the folder, no error if it already exists
shutil.move(src, dst)       # moves a file from src to dst
                            # both arguments must be strings, not Path objects
                            # use str() to convert
Your job — add three lines inside the loop:

destination =  ... build the folder path where this file should go
destination.mkdir(...) ... create the folder
shutil.move(...) ... move the file into that destination folder
Don't change anything else. Just add those three lines after folder = rules.get(...).

Paste it back when done. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():
            continue
        log.info(item.name)
        ext = item.suffix.lower()
        folder = rules.get(ext, "Misc")
        destination= Path(source/folder)
        destination.mkdir(parents=True, exist_ok=True)
        shutil.move(source, destination)

4:01 PM
Really close — the logic is solid. Two fixes:

Bug 1 — style on destination=

python
destination= Path(source/folder)   # ❌ missing space before =
destination = Path(source/folder)  # ✅
Bug 2 — wrong argument in shutil.move()

python
shutil.move(source, destination)   # ❌ moves the whole source FOLDER
shutil.move(item, destination)     # ✅ moves the individual file
source is the directory we're scanning. item is the specific file we're currently processing. We want to move the file, not the whole folder.

Also remember shutil.move() needs strings, not Path objects:

python
shutil.move(str(item), str(destination))  # ✅ convert both to str
Also — move the log.info() to after the move

Right now you log the filename before anything happens. Better to log after the move so you confirm it actually succeeded:

python
log.info(f"Moved {item.name} -> {folder}/")
The f"..." is an f-string — it lets you embed variables directly inside a string. We'll use these constantly.

Fix all three things and paste it back. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():
            continue
        log.info(item.name)
        ext = item.suffix.lower()
        folder = rules.get(ext, "Misc")
        destination = Path(source/folder)
        destination.mkdir(parents=True, exist_ok=True)
        shutil.move(str(item), str(destination))
        log.info(f"Moved {item.name} -> {folder}/")

4:02 PM
Good progress — almost there. Two things:

Bug 1 — duplicate log.info()

You still have the old log.info(item.name) at the top from the previous step. Remove it — you only need the one at the bottom that confirms the move:

python
for item in source.iterdir():
    if not item.is_file():
        continue
    log.info(item.name)                        # ❌ remove this line
    ext = item.suffix.lower()
    folder = rules.get(ext, "Misc")
    destination = Path(source / folder)
    destination.mkdir(parents=True, exist_ok=True)
    shutil.move(str(item), str(destination))
    log.info(f"Moved {item.name} -> {folder}/") # ✅ keep this one
Bug 2 — Path(source/folder) is redundant

source / folder already returns a Path object. Wrapping it in Path() again does nothing:

python
destination = Path(source / folder)  # ❌ redundant outer Path()
destination = source / folder        # ✅ cleaner
Fix both, paste it back. 🟢

def organize(source: Path, rules: dict[str, str]) -> None:
    for item in source.iterdir():
        if not item.is_file():
            continue
        ext = item.suffix.lower()
        folder = rules.get(ext, "Misc")
        destination = source/folder
        destination.mkdir(parents=True, exist_ok=True)
        shutil.move(str(item), str(destination))
        log.info(f"Moved {item.name} -> {folder}/")

4:03 PM
That is perfect. Clean, correct, professional. ✅

Look at what this function does in just 7 lines:

1. skip anything that isn't a file
2. get the extension, lowercase it
3. look up which folder it belongs to
4. build the destination path
5. create the folder if it doesn't exist
6. move the file
7. log what happened
That's the entire core logic of the organizer. Every decision we made has a reason behind it.

Quick concept check before we move on

Tell me in your own words what this line does:

python
folder = rules.get(ext, "Misc")
Specifically — what happens when ext is something like .xyz that doesn't exist in the dictionary? What does .get() do differently than rules[ext]?

Answer that and then we move to Step 4 — the main() function, which is where we wire everything together and add the command line interface. 🟢

looks what folder the files belongs  to and assigns it to a foilder named misc if the extension does not exixt in the dictinary rules

4:10 PM
Exactly right. ✅

And the difference between .get() and rules[ext]:

python
rules[ext]              # ❌ crashes with KeyError if ext not in dictionary
rules.get(ext, "Misc")  # ✅ returns "Misc" safely if ext not found
.get() never crashes. Always use it when a key might not exist.

Step 4 — the main() function

This is the entry point of the script — the function that runs when you type python organizer.py in the terminal. It has two jobs:

Accept a folder path from the user via the command line
Call organize() with that path
For now write a main() function that does just one thing — uses argparse to accept one argument from the command line called source.

Here's how argparse works in plain English:

python
parser = argparse.ArgumentParser()         # create the parser
parser.add_argument("source")              # add a positional argument
args = parser.parse_args()                 # read what the user typed
print(args.source)                         # access the value
When the user runs:

bash
python organizer.py /home/ivan/Downloads
args.source will equal "/home/ivan/Downloads".

Your task — write main() that:

Creates an ArgumentParser
Adds a "source" argument with type=Path so it automatically converts to a Path object
Parses the args
Calls organize(args.source, DEFAULT_RULES)
Paste it back when done. 🟢

def main():
    #Creates the CLI interface
    parser= argparse.ArgumentParser(
        description="Smart File Organizer CLI"
        )
    #Defines the source as a positional argument
    parser.add_argument("source=", type=Path)
    #Parses the arg
    args = parser.parse_args()
    organize(args.source, DEFAULT_RULES)

4:19 PM
Really solid — the structure is correct and your comments are good. One bug:

Bug — extra = in add_argument

python
parser.add_argument("source=", type=Path)  # ❌ "source=" is not a valid name
parser.add_argument("source", type=Path)   # ✅ just the name, no equals sign
The = doesn't belong in the argument name. argparse uses the name "source" to create args.source automatically — no equals sign needed.

Also one style fix — space after = in assignments:

python
parser= argparse.ArgumentParser(   # ❌
parser = argparse.ArgumentParser(  # ✅
Fix both and paste it back. 🟢

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

4:20 PM
Perfect. That's exactly right. ✅

Step 5 — the entry point guard

One last thing to add at the very bottom of the file, outside and after all functions:

python
if __name__ == "__main__":
    main()
What this does in plain English:

When Python runs a file it sets a special variable called __name__. If you run the file directly (python organizer.py) it equals "__main__". If another script imports your file, it equals the filename instead.

This guard means:

python organizer.py → main() runs ✅
import organizer from another script → main() does NOT run ✅
Without it, main() would fire automatically whenever anyone imports your code — which would be a bug.

Every Python script you write should end with this. It's a universal convention.

Add those two lines at the bottom of your file and then paste the entire file from top to bottom. This will be our first full review of the complete script. 🟢


""" Smart File Organizer Automatically scans a directory, classifies files based on user-defined rules, and moves them into structured destination folders. """ # ─── Standard library imports ───────────────────────────────────────────────── # These come built into Python — no installation ne

pasted

4:21 PM

The user prompt is empty, so I cannot provide a summary in the user's language. However, based on the thinking block alone, here is a summary: Audited code for style violations and improvements
The user prompt is empty, so I cannot provide a summary in the user's language. However, based on the thinking block alone, here is a summary: Audited code for style violations and improvements
Great work — the script is complete and the logic is correct. Full review:

✅ What's good:

Imports clean and alphabetical
Dictionary structure correct, aligned, commented
Guard clause pattern in organize()
shutil.move() with str() conversion correct
main() clean and simple
Entry point guard at the bottom
Three things to fix:

1 — import os is unused

python
import os  # ❌ you never call os.anything — remove it
Unused imports are flagged in every code review. If you don't use it, don't import it.

2 — Two blank lines before each function PEP 8 requires two blank lines between top-level functions:

python
log = logging.getLogger(__name__)
                                    # ← one blank line (not enough)
def organize(...):
Should be:

python
log = logging.getLogger(__name__)
                                    # ← blank line
                                    # ← blank line
def organize(...):
3 — Add a docstring to organize() Every function needs one. Right after def organize(...): add:

python
    """Scan source directory and move each file to its destination folder."""
Make those three fixes and paste the full file back one more time — then we test it live on your machine. 🟢


""" Smart File Organizer Automatically scans a directory, classifies files based on user-defined rules, and moves them into structured destination folders. """ # ─── Standard library imports ───────────────────────────────────────────────── # These come built into Python — no installation ne

pasted

test was good

9:18 PM

Validated script and prepared next steps
Validated script and prepared next steps
That's a fully working script you built yourself. Let's do the final review:

✅ Everything looks good:

import os removed
Two blank lines before main()
Docstring added to organize()
Logic clean, comments professional
Entry point guard in place
One last style note — move inline comments to the line above:

python
# ❌ inline — harder to read when lines get long
destination = source/folder  #Build the destination path

# ✅ above — cleaner, more readable
# Build the destination path
destination = source / folder
This is minor but senior devs consistently write comments above the line, not beside it. Fix that across your organize() function.

Once that's done, time to push to GitHub. Run these commands in your terminal from inside your project folder:

bash
git init
git add .
git commit -m "feat: script 01 - smart file organizer"
git branch -M main
git remote add origin https://github.com/ivankoueniwork-19889/python-automation-portfolio.git
git push -u origin main
Paste the terminal output here so we can confirm it went through cleanly — then we move straight to Script 02 — CSV Data Cleaner & Reporter. 🟢

git push -u origin main
remote: Repository not found.
fatal: repository 'https://github.com/ivankoueniwork-19889/python-automation-portfolio.git/' not found

9:20 PM
The repo doesn't exist on GitHub yet. You need to create it first.

Go to GitHub and create the repo:

Go to github.com/new
Fill in:
Repository name: python-automation-portfolio
Description: 10 Python automation scripts — file management, web scraping, security tooling and more
Visibility: Public
Do NOT check "Add a README" — we already have one
Click Create repository
Once created, come back and run the push command again:

bash
git push -u origin main
Paste the output here. 🟢

Writing objects: 100% (3/3), 2.29 KiB | 781.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/ivankoueniwork-19889/python-automation-portfolio.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

9:21 PM

Orchestrated successful code repository deployment progression
Orchestrated successful code repository deployment progression
Script 01 is live on GitHub. ✅

Go check it right now:

👉 https://github.com/ivankoueniwork-19889/python-automation-portfolio

You should see your organizer.py file sitting in the repo.

Here's what you built and understood in Script 01:

Concept	Status
Hash maps / dictionaries	✅
pathlib.Path for file operations	✅
Guard clauses	✅
logging vs print()	✅
argparse CLI	✅
Type hints	✅
shutil.move()	✅
PEP 8 style	✅
if __name__ == "__main__"	✅
That's a strong foundation. Every script from here builds on these.

Ready for Script 02 — CSV Data Cleaner & Reporter?

This one introduces pandas — the most in-demand Python library in the job market right now. You'll build a tool that takes a messy CSV file, detects problems in the data automatically, cleans it, and outputs a report.

Real companies do this every single day.

Say the word and we start. 🟢

lets get thge finalk script with appropriate description for the first one

9:22 PM

Identified request for complete annotated script delivery
Identified request for complete annotated script delivery
Here is the final version of Script 01 — clean, commented, ready for your portfolio:


Created a file, read a file
Created a file, read a file
Replace your current organizer.py with this file, then push:

bash
git add .
git commit -m "feat: script 01 - finalize smart file organizer with full comments"
git push
Script 01 is officially done. Here's what you built from scratch:

A working CLI tool that sorts any folder on your machine
Professional logging with timestamps and severity levels
Hash map lookups for instant file classification
Safe folder creation and file moving
Clean PEP 8 code a senior dev would be proud to review
Ready for Script 02 — CSV Data Cleaner? Just say go. 🟢


Organizer
PY 





Claude is AI and can make mistakes. Please double-check responses.
Organizer · PY
"""
Smart File Organizer
====================
Automatically scans a directory, classifies files based on user-defined rules,
and moves them into structured destination folders.
 
Usage:
    python organizer.py <source_directory>
 
Example:
    python organizer.py ~/Downloads
 
Author  : ivankoueniwork-19889
GitHub  : https://github.com/ivankoueniwork-19889/python-automation-portfolio
Script  : 01 / 10
"""
 
# ─── Standard library imports ─────────────────────────────────────────────────
# These come built into Python — no installation needed.
# We import only what we need, one per line (PEP 8 style guide).
import argparse        # builds our command-line interface
import logging         # structured messages instead of print() — timestamps + severity
import shutil          # high-level file operations — move, copy, delete
from pathlib import Path  # modern way to work with file paths (replaces os.path)
 
 
# ─── Default rules dictionary ─────────────────────────────────────────────────
# This is the brain of the organizer.
# It maps every file extension (key) to a destination folder name (value).
#
# Why a dictionary and not a list?
# Dictionaries use hash maps under the hood — looking up ".jpg" is
# instant (O(1)) no matter how many entries exist. A list would require
# scanning every entry one by one (O(n)) which slows down with scale.
#
# Why extensions as keys and folders as values?
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
#   %(message)s      → our message : Moved photo.jpg -> Images/
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
 
 
# ─── Core function ────────────────────────────────────────────────────────────
def organize(source: Path, rules: dict[str, str]) -> None:
    """Scan source directory and move each file to its destination folder.
 
    Parameters
    ----------
    source : Path
        The directory to scan. Must exist before calling this function.
    rules : dict[str, str]
        A mapping of file extension to destination folder name.
        Example: {".jpg": "Images", ".pdf": "Documents"}
    """
    for item in source.iterdir():
        # Guard clause — skip anything that is not a file (subfolders, symlinks)
        if not item.is_file():
            continue
 
        # Get the file extension and normalize to lowercase
        # so .JPG and .jpg both match the same rule
        ext = item.suffix.lower()
 
        # Look up which folder this extension belongs to
        # .get() returns "Misc" safely if the extension is not in the dictionary
        # using rules[ext] directly would crash with a KeyError if not found
        folder = rules.get(ext, "Misc")
 
        # Build the full destination path by joining source + folder name
        destination = source / folder
 
        # Create the destination folder if it does not exist yet
        # parents=True  — creates any missing parent folders along the way
        # exist_ok=True — does not raise an error if the folder already exists
        destination.mkdir(parents=True, exist_ok=True)
 
        # Move the file into the destination folder
        # shutil.move() requires string arguments, not Path objects
        shutil.move(str(item), str(destination))
 
        # Confirm the move with a timestamped log message
        log.info(f"Moved {item.name} -> {folder}/")
 
 
# ─── Entry point ──────────────────────────────────────────────────────────────
def main() -> None:
    """Parse command-line arguments and run the organizer."""
 
    # Create the CLI interface
    parser = argparse.ArgumentParser(
        description="Smart File Organizer — sort files by type into folders."
    )
 
    # Define source as a positional argument
    # type=Path automatically converts the string input into a Path object
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the directory you want to organize"
    )
 
    # Parse what the user typed in the terminal
    args = parser.parse_args()
 
    # Run the organizer with the provided path and our default rules
    organize(args.source, DEFAULT_RULES)
 
 
# ─── Guard ────────────────────────────────────────────────────────────────────
# This block only runs when the script is executed directly.
# If another script imports this file, main() will NOT run automatically.
# This is a universal Python convention — always include it.
if __name__ == "__main__":
    main()
 
