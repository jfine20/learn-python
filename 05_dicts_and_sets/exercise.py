print("=" * 50)
print("MODULE 5: Dicts & Sets")
print("=" * 50)

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: Why dict lookups are instant ---")
# ─────────────────────────────────────────────────

# A dict is backed by a HASH TABLE.
# When you do d["key"], Python:
#   1. Calls hash("key") → converts the key to a number
#   2. Uses that number to jump directly to the right memory slot
#   3. Returns the value
#
# This is O(1) — same speed whether the dict has 10 or 10 million items.
# A list lookup by value is O(n) — it checks every item until it finds it.

print("Hash values (what Python computes internally for keys):")
for key in ["hello", "world", 42, (1, 2)]:
    print(f"  hash({key!r:12}) = {hash(key)}")

print("\nOnly IMMUTABLE objects can be keys (their hash must never change):")
d = {}
d["string key"] = "works"
d[42]           = "works"
d[(1, 2)]       = "works"   # tuple works if contents are immutable
print(f"  Valid keys: {list(d.keys())}")

try:
    d[[1, 2]] = "fails"
except TypeError as e:
    print(f"  List as key → TypeError: {e}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: Reading from dicts safely ---")
# ─────────────────────────────────────────────────

user = {"name": "Jack", "role": "founder", "age": 28}

print("Direct access — crashes if key missing:")
print(f"  user['name'] = {user['name']}")

print("\n.get() — returns None (or a default) if key missing:")
print(f"  user.get('name')        = {user.get('name')}")
print(f"  user.get('salary')      = {user.get('salary')}")
print(f"  user.get('salary', 0)   = {user.get('salary', 0)}")

print("\nIterating:")
for key, value in user.items():
    print(f"  {key}: {value}")

print("\nDict comprehension:")
lengths = {word: len(word) for word in ["apple", "banana", "kiwi"]}
print(f"  word lengths: {lengths}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: Merging and updating dicts ---")
# ─────────────────────────────────────────────────

defaults = {"color": "blue", "size": "medium", "weight": 1.0}
overrides = {"color": "red", "size": "large"}

# Python 3.9+ merge with |
merged = defaults | overrides
print(f"  defaults | overrides = {merged}")
print(f"  defaults unchanged   = {defaults}")

# Update in place
defaults.update(overrides)
print(f"  after .update():     = {defaults}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: Sets ---")
# ─────────────────────────────────────────────────

# A set is like a dict with only keys (no values).
# Same hash table, same O(1) lookup.
# Primary uses: deduplication, membership testing, set math.

print("Deduplication:")
with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(with_dupes))
print(f"  {with_dupes} → {unique}")

print("\nMembership — sets are MUCH faster than lists for `in` checks:")
big_list = list(range(1_000_000))
big_set  = set(range(1_000_000))
# Checking `999_999 in big_list` scans up to 1M items
# Checking `999_999 in big_set` is one hash lookup
print(f"  999999 in set:  {999999 in big_set}")

print("\nSet operations:")
a = {"alice", "bob", "carol"}
b = {"bob", "carol", "dave"}
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  a & b (intersection) = {a & b}")   # in both
print(f"  a | b (union)        = {a | b}")   # in either
print(f"  a - b (difference)   = {a - b}")   # in a but not b
print(f"  a ^ b (symmetric diff) = {a ^ b}") # in one but not both

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Add your code below. Save and run after each one.

1. Count word frequencies. Given:
     text = "the cat sat on the mat the cat sat"
   Build a dict: {"the": 3, "cat": 2, ...}
   Do it with a loop and .get(), then check your answer using collections.Counter.

2. Given this list of users, find all users whose role is "engineer":
     users = [
         {"name": "Alice", "role": "engineer"},
         {"name": "Bob",   "role": "founder"},
         {"name": "Carol", "role": "engineer"},
     ]
   Use a list comprehension.

3. You have two sets of email addresses:
     list_a = {"alice@x.com", "bob@x.com", "carol@x.com"}
     list_b = {"bob@x.com", "carol@x.com", "dave@x.com"}
   Print: who is in BOTH lists, who is ONLY in list_a, everyone combined.
""")

# YOUR CODE HERE ↓
