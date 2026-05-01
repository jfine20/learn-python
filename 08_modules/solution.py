# Module 08 — Solutions
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# ── Exercise 1 ────────────────────────────────────────────────────────────────
print(sys.path)    # first entry is '' (empty string) = current directory
print(sys.version) # Python version string

# ── Exercise 2 ────────────────────────────────────────────────────────────────
data = {"name": "Jack", "scores": [95, 87, 92], "active": True, "address": None}

json_str = json.dumps(data, indent=2)
print(json_str)

restored = json.loads(json_str)
print(restored == data)  # True — perfect round-trip
# Note: None ↔ null, True ↔ true, False ↔ false

# ── Exercise 3 ────────────────────────────────────────────────────────────────
now = datetime.now()
print(now.strftime("%B %d, %Y at %H:%M"))

future = now + timedelta(days=30)
print(future.date())

# ── Exercise 4 ────────────────────────────────────────────────────────────────
cwd = Path.cwd()
print(cwd)

notes = cwd / "docs" / "notes.txt"
print(notes.name)    # notes.txt
print(notes.stem)    # notes
print(notes.suffix)  # .txt
print(notes.parent)  # .../docs

# ── Exercise 5 ────────────────────────────────────────────────────────────────
grades = [
    ("alice", 90), ("bob", 85), ("alice", 92),
    ("bob", 78), ("charlie", 88), ("alice", 95),
]

student_grades = defaultdict(list)
for student, grade in grades:
    student_grades[student].append(grade)  # no KeyError — missing key → empty list

for student, g in student_grades.items():
    avg = sum(g) / len(g)
    print(f"{student}: {g} → avg {avg:.1f}")

# ── Exercise 6 ────────────────────────────────────────────────────────────────
def main():
    print("Running as script")

# Without this guard, `main()` would run whenever ANY file imported this module.
# That causes side effects during import — printing, network calls, etc.
# The guard means: only run this code if I am the entry point.
if __name__ == "__main__":
    main()
