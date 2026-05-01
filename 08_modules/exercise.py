# Module 08 — Modules
# Run: python 08_modules/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Explore sys.path — where Python looks for modules.
import sys
# TODO: print sys.path. What's the first entry?
# Then print sys.version.


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# json — serialize and deserialize.
import json

data = {
    "name": "Jack",
    "scores": [95, 87, 92],
    "active": True,
    "address": None,
}

# TODO:
#   a) convert `data` to a JSON string using json.dumps() with indent=2
#   b) convert it back to a Python dict using json.loads()
#   c) verify the round-trip was lossless using ==


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# datetime — work with dates.
from datetime import datetime, timedelta

# TODO:
#   a) get today's date and time: datetime.now()
#   b) format it as a readable string: "April 30, 2026 at 14:32"
#      (hint: strftime with %B, %d, %Y, %H, %M)
#   c) calculate the date 30 days from now using timedelta


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# pathlib — modern file paths. Better than string concatenation.
from pathlib import Path

# TODO:
#   a) get the current directory: Path.cwd()
#   b) build a path to a (hypothetical) file "notes.txt" in a subdirectory "docs"
#      using / operator (pathlib overloads it)
#   c) print the file's name, stem (no extension), suffix, and parent


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# collections.defaultdict — a dict that provides a default for missing keys.
from collections import defaultdict

# TODO: given this list of (student, grade) tuples, build a dict
# mapping each student to a LIST of their grades.
# Use defaultdict(list) to avoid checking if the key exists first.
grades = [
    ("alice", 90), ("bob", 85), ("alice", 92),
    ("bob", 78), ("charlie", 88), ("alice", 95),
]


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# __name__ == "__main__"
# TODO: write a function `main()` below that prints "Running as script".
# Then add the if __name__ == "__main__": guard so it only runs when this
# file is executed directly.
# Explain in a comment: what would happen if another file did `import exercise`
# without this guard?

def main():
    pass  # TODO
