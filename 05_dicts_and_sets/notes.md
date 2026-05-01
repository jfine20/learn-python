# Module 5: Dicts & Sets

## What is a dict?

A dict (dictionary) maps **keys** to **values**. Like a real dictionary maps words to definitions. You look up a key and instantly get the value back.

---

## Step 1: Creating and reading dicts

```python
user = {
    "name": "Jack",
    "age": 28,
    "role": "founder"
}

print(user["name"])
print(user["age"])
print(len(user))
```

**What you should see:** `Jack`, `28`, `3`

---

## Step 2: Safe access with .get()

If you try to access a key that doesn't exist, Python crashes:

```python
user = {"name": "Jack"}
print(user["salary"])   # KeyError!
```

Use `.get()` instead — it returns `None` (or a default you choose) if the key is missing:

```python
user = {"name": "Jack"}
print(user.get("name"))           # Jack
print(user.get("salary"))         # None — no crash
print(user.get("salary", 0))      # 0 — your chosen default
```

---

## Step 3: Adding, updating, deleting

```python
user = {"name": "Jack", "age": 28}

user["role"] = "founder"          # add new key
user["age"] = 29                  # update existing key
del user["age"]                   # delete a key

print(user)
```

---

## Step 4: Looping over dicts

```python
person = {"name": "Jack", "age": 28, "city": "NYC"}

# Just keys
for key in person:
    print(key)

# Just values
for value in person.values():
    print(value)

# Keys AND values (most common)
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Step 5: Why dict lookups are instant — hash tables

When you do `user["name"]`, Python doesn't scan through all the keys. It:
1. Calls `hash("name")` — converts the key to a number
2. Jumps directly to that memory slot
3. Returns the value

This is **O(1)** — same speed with 10 items or 10 million items. This is why dicts are one of Python's most important data structures.

Because of this, only **immutable** objects can be keys (their hash must never change):

```python
d = {}
d["string"] = "works"
d[42] = "works"
d[(1, 2)] = "works"    # tuple of immutables — works

try:
    d[[1, 2]] = "fails"
except TypeError as e:
    print(e)
```

---

## Step 6: Dict comprehensions

Just like list comprehensions, but produces a dict:

```python
words = ["apple", "banana", "kiwi", "fig"]
lengths = {word: len(word) for word in words}
print(lengths)
```

**What you should see:** `{'apple': 5, 'banana': 6, 'kiwi': 4, 'fig': 3}`

---

## Step 7: Counting things with a dict

A very common pattern:

```python
text = "the cat sat on the mat the cat"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

**What you should see:** Each word mapped to how many times it appears.

**Shortcut with Counter:**

```python
from collections import Counter
counts = Counter(text.split())
print(counts)
print(counts.most_common(3))
```

---

## Step 8: Sets

A set is like a dict but with only keys — no values. It's built on the same hash table, so lookups are also instant. Use sets for:

- **Deduplication** — remove duplicates from a list
- **Membership testing** — `if x in my_set` is much faster than `if x in my_list`
- **Set math** — find overlap, union, difference between groups

```python
a = {"alice", "bob", "carol"}
b = {"bob", "carol", "dave"}

print(a & b)    # intersection — who's in both
print(a | b)    # union — everyone
print(a - b)    # difference — in a but not b
```

**Remove duplicates from a list:**

```python
with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(with_dupes))
print(unique)
```

---

## Now try it yourself

```python
# You have a list of (student, grade) pairs.
# Build a dict that maps each student to their AVERAGE grade.

grades = [
    ("alice", 90), ("bob", 85), ("alice", 92),
    ("bob", 78), ("charlie", 95), ("alice", 88),
]

# Step 1: group grades by student into lists
# Step 2: calculate the average for each student
# Expected output: {'alice': 90.0, 'bob': 81.5, 'charlie': 95.0}
```
