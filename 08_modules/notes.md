# Module 8: Modules & the Standard Library

## What is a module?

A module is just a `.py` file. When you `import` it, Python runs the file top-to-bottom and makes everything in it available to you.

Python ships with hundreds of modules built in — the **standard library**. You also install third-party ones with `pip`.

---

## Step 1: Importing

```python
import math

print(math.pi)
print(math.sqrt(16))
print(math.floor(3.7))
print(math.ceil(3.2))
```

**What you should see:** `3.14159...`, `4.0`, `3`, `4`

Three ways to import:

```python
import math                    # access with math.sqrt()
from math import sqrt          # access directly as sqrt()
from math import sqrt as sq    # aliased to sq()
```

---

## Step 2: json — save and load data

JSON is the most common format for sending and storing data. Python's `json` module converts between Python objects and JSON text.

```python
import json

# Python dict → JSON string
data = {
    "name": "Jack",
    "scores": [95, 87, 92],
    "active": True,
    "address": None,
}

text = json.dumps(data, indent=2)
print(text)

# JSON string → Python dict
restored = json.loads(text)
print(restored == data)
print(type(restored))
```

**What you should see:** Formatted JSON text, then `True`, then `<class 'dict'>`

Note the conversions: Python `None` ↔ JSON `null`, Python `True` ↔ JSON `true`.

---

## Step 3: datetime — working with dates and times

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now.strftime("%B %d, %Y"))     # e.g. "April 30, 2026"
print(now.strftime("%A"))            # day of the week

# Math with dates
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(tomorrow.date())
print(last_week.date())

# Days between two dates
new_years = datetime(2027, 1, 1)
days_until = (new_years - now).days
print(f"Days until 2027: {days_until}")
```

---

## Step 4: pathlib — file paths the right way

```python
from pathlib import Path

# Get locations
print(Path.cwd())      # current directory
print(Path.home())     # home directory (~)

# Build paths with / operator
project = Path.home() / "learn-python"
readme = project / "README.md"

print(readme)
print(readme.name)      # "README.md"
print(readme.stem)      # "README"
print(readme.suffix)    # ".md"
print(readme.parent)    # the learn-python folder
print(readme.exists())  # True or False
```

**Why not just use strings?** Pathlib handles `/` vs `\` on different OS, avoids string concatenation bugs, and has helpful methods built in.

---

## Step 5: collections — powerful data structures

```python
from collections import Counter, defaultdict

# Counter counts things
text = "the quick brown fox jumps over the lazy dog"
word_counts = Counter(text.split())
print(word_counts.most_common(3))

# Count characters in a string
letter_counts = Counter(text.replace(" ", ""))
print(letter_counts.most_common(5))
```

```python
from collections import defaultdict

# defaultdict avoids KeyError by creating a default for missing keys
groups = defaultdict(list)

data = [("Alice", "eng"), ("Bob", "design"), ("Alice", "eng"), ("Carol", "eng")]
for name, dept in data:
    groups[dept].append(name)    # no KeyError if dept is new

for dept, people in groups.items():
    print(f"{dept}: {people}")
```

---

## Step 6: sys — Python runtime info

```python
import sys

print(sys.version)          # Python version
print(sys.platform)         # "darwin", "win32", "linux"
print(sys.path[:3])         # where Python looks for modules
```

---

## Step 7: if __name__ == "__main__"

When Python runs a file directly, `__name__` is `"__main__"`. When it's imported by another file, `__name__` is the filename.

This guard lets you write code that only runs when you execute the file directly — not when it's imported:

```python
def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("World"))

if __name__ == "__main__":
    main()
```

Without this guard, `main()` would run every time anyone imported this file — even if they only wanted to use `greet()`.

---

## Now try it yourself

```python
import json
from datetime import datetime
from pathlib import Path

# 1. Create a dict about yourself with: name, age, skills (list), joined_date
# 2. Save it to a file called "profile.json" using json.dump()
#    Hint: open("profile.json", "w") as f: then json.dump(data, f, indent=2)
# 3. Read it back using json.load()
#    Hint: open("profile.json") as f: then json.load(f)
# 4. Print how old the file is in seconds using datetime
#    Hint: Path("profile.json").stat().st_mtime gives the creation timestamp
```
