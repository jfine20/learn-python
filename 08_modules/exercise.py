print("=" * 50)
print("MODULE 8: Modules & the Standard Library")
print("=" * 50)

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: How import works ---")
# ─────────────────────────────────────────────────

# A module is just a .py file. When you `import` it, Python:
#   1. Finds the file (searches sys.path)
#   2. Runs the file top-to-bottom
#   3. Makes its names available to you
#
# Python caches imports — importing the same module twice doesn't re-run it.

import sys

print("Where Python looks for modules (sys.path):")
for i, path in enumerate(sys.path[:5]):
    print(f"  [{i}] {path or '(current directory)'}")
print(f"  ... ({len(sys.path)} total paths)")

print(f"\nPython version: {sys.version.split()[0]}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: json ---")
# ─────────────────────────────────────────────────

import json

# json.dumps() → Python object to JSON string
# json.loads() → JSON string back to Python object
# Python None ↔ JSON null
# Python True ↔ JSON true

data = {
    "name": "Jack",
    "scores": [95, 87, 92],
    "active": True,
    "address": None,
}

json_string = json.dumps(data, indent=2)
print("Python dict → JSON string:")
print(json_string)

restored = json.loads(json_string)
print(f"\nRound-trip successful: {data == restored}")
print(f"Type of restored: {type(restored)}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: datetime ---")
# ─────────────────────────────────────────────────

from datetime import datetime, timedelta

now = datetime.now()
print(f"Now:             {now}")
print(f"Formatted:       {now.strftime('%B %d, %Y at %H:%M')}")
print(f"Just the date:   {now.date()}")
print(f"Just the time:   {now.time()}")

tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"\nTomorrow:  {tomorrow.date()}")
print(f"Last week: {last_week.date()}")

# Difference between two datetimes
start = datetime(2026, 1, 1)
delta = now - start
print(f"\nDays since Jan 1 2026: {delta.days}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: pathlib ---")
# ─────────────────────────────────────────────────

from pathlib import Path

# pathlib is the modern way to work with file paths.
# It uses / to join paths (overloads the operator).

cwd = Path.cwd()
print(f"Current directory: {cwd}")
print(f"Home directory:    {Path.home()}")

# Build paths with /
my_file = Path.home() / "learn-python" / "README.md"
print(f"\nPath:    {my_file}")
print(f"Name:    {my_file.name}")
print(f"Stem:    {my_file.stem}")
print(f"Suffix:  {my_file.suffix}")
print(f"Parent:  {my_file.parent}")
print(f"Exists:  {my_file.exists()}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 5: collections ---")
# ─────────────────────────────────────────────────

from collections import Counter, defaultdict

# Counter — counts hashable objects
text = "the quick brown fox jumps over the lazy dog"
word_counts = Counter(text.split())
print("Most common words:")
for word, count in word_counts.most_common(5):
    print(f"  '{word}': {count}")

# defaultdict — a dict that creates a default value for missing keys
print("\ndefaultdict — grouping items:")
grades = [("alice", 90), ("bob", 85), ("alice", 92), ("bob", 78)]
by_student = defaultdict(list)
for name, grade in grades:
    by_student[name].append(grade)   # no KeyError — missing key → empty list

for name, g in by_student.items():
    print(f"  {name}: {g}  avg={sum(g)/len(g):.1f}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 6: __name__ == '__main__' ---")
# ─────────────────────────────────────────────────

# When Python runs a file directly, __name__ is "__main__".
# When a file is imported by another file, __name__ is the module's filename.
# This guard lets you write code that only runs when executed directly.

print(f"__name__ = '{__name__}'")
print("Since we ran this file directly, __name__ is '__main__'.")
print("If another file did `import exercise`, __name__ would be 'exercise'")
print("and any code inside `if __name__ == '__main__':` would NOT run.")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Add your code below. Save and run after each one.

1. Use json to save a dict to a file and load it back.
   - Create a dict with your name, age, and a list of 3 hobbies
   - Write it to a file called "me.json" using json.dump() (note: dump not dumps)
   - Read it back using json.load() and print it
   - Hint: open("me.json", "w") for writing, open("me.json") for reading

2. Use datetime to calculate:
   - How many days until January 1, 2027
   - What day of the week today is (hint: .strftime('%A'))

3. Use Counter to find the 3 most common CHARACTERS (not words) in this string:
   text = "python programming is pretty powerful"
   (Hint: Counter works on any iterable — including a string directly)
""")

# YOUR CODE HERE ↓

if __name__ == "__main__":
    pass  # your code above will run regardless — this is just here to show the pattern
