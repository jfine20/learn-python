# Module 05 — Solutions
from collections import Counter

# ── Exercise 1 ────────────────────────────────────────────────────────────────
d = {}
try:
    d[[1, 2]] = "list key"
except TypeError as e:
    print(f"List as key failed: {e}")

d[(1, 2)] = "tuple key works"
print(d)
# Lists are mutable — their contents can change, so their hash would change.
# A hash table requires stable hashes. Tuples are immutable, so their hash is fixed.

# ── Exercise 2 ────────────────────────────────────────────────────────────────
user = {"name": "Jack", "role": "founder"}
print(user["name"])                    # Jack
print(user.get("missing", "unknown"))  # unknown
print(user["missing"] if "missing" in user else "unknown")  # unknown

# ── Exercise 3 ────────────────────────────────────────────────────────────────
words = ["apple", "banana", "cherry", "kiwi"]
lengths = {w: len(w) for w in words}
print(lengths)

# ── Exercise 4 ────────────────────────────────────────────────────────────────
text = "the cat sat on the mat the cat sat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)

# Shortcut:
print(Counter(text.split()))

# ── Exercise 5 ────────────────────────────────────────────────────────────────
emails_a = {"alice@x.com", "bob@x.com", "carol@x.com"}
emails_b = {"bob@x.com", "carol@x.com", "dave@x.com"}

print(emails_a & emails_b)  # intersection: {'bob@x.com', 'carol@x.com'}
print(emails_a | emails_b)  # union: all 4
print(emails_a - emails_b)  # difference: {'alice@x.com'}

dupes = [1, 2, 2, 3, 3, 3, 4]
print(list(set(dupes)))     # [1, 2, 3, 4] (order not guaranteed for sets)

# ── Exercise 6 ────────────────────────────────────────────────────────────────
users = {
    "jack":  {"age": 28, "role": "founder"},
    "alice": {"age": 34, "role": "engineer"},
    "bob":   {"age": 22, "role": "intern"},
}

for username, info in users.items():
    print(f"{username}: {info['role']}")

older = [name for name, info in users.items() if info["age"] > 25]
print(older)

users["carol"] = {"age": 30, "role": "designer"}

salary = users["jack"].get("salary", None)
print(salary)  # None — no crash
