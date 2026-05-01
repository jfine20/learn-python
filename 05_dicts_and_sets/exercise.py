# Module 05 — Dicts & Sets
# Run: python 05_dicts_and_sets/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Only hashable (immutable) objects can be dict keys.
# TODO: try using a list as a dict key and catch the TypeError.
# Then try a tuple. Then explain in a comment why tuples work but lists don't.


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# Safe access patterns.
user = {"name": "Jack", "role": "founder"}
# TODO:
#   a) get the "name" key
#   b) get a "missing" key without crashing — return "unknown" as default
#   c) get "missing" using a conditional expression (not .get) — one line


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# Dict comprehension.
words = ["apple", "banana", "cherry", "kiwi"]
# TODO: build a dict mapping each word to its length: {"apple": 5, ...}


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# Count word frequencies using a dict.
text = "the cat sat on the mat the cat sat"
# TODO: build a dict: {"the": 3, "cat": 2, ...}
# Do it manually with a loop first. Then try collections.Counter as a shortcut.


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# Sets for deduplication and membership.
emails_a = {"alice@x.com", "bob@x.com", "carol@x.com"}
emails_b = {"bob@x.com", "carol@x.com", "dave@x.com"}

# TODO:
#   a) who is in both lists? (intersection)
#   b) everyone across both lists, no duplicates (union)
#   c) who is only in list A? (difference)
#   d) remove duplicates from: [1, 2, 2, 3, 3, 3, 4] using a set


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# Nested dicts — representing structured data.
users = {
    "jack":  {"age": 28, "role": "founder"},
    "alice": {"age": 34, "role": "engineer"},
    "bob":   {"age": 22, "role": "intern"},
}
# TODO:
#   a) print all usernames and their roles
#   b) find all users older than 25
#   c) add a new user "carol" with age 30, role "designer"
#   d) safely get the "salary" field for "jack" without crashing
