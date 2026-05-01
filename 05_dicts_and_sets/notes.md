# Dicts & Sets — Why Lookups Are Instant

## The hash table

A dict (and set) is backed by a **hash table**. Here's what happens when you do
`d["key"]`:

1. Python calls `hash("key")` — converts the key to an integer (the hash)
2. Uses the hash to jump directly to a memory slot
3. Returns the value at that slot

This is O(1) — constant time regardless of dict size. A list lookup by value
is O(n) — it has to check every item.

```python
import timeit
big_list = list(range(1_000_000))
big_dict = {i: i for i in range(1_000_000)}

# Looking up 999_999 in a list: scans up to a million items
# Looking up 999_999 in a dict: one hash computation, done
```

## Keys must be hashable

Because keys need a stable hash, only **immutable** objects can be keys:
`str`, `int`, `float`, `tuple` (if its contents are also immutable).

`list`, `dict`, `set` cannot be dict keys — they're mutable, so their
content (and thus their hash) could change.

```python
d = {}
d[(1, 2)] = "tuple key works"   # ok
d[[1, 2]] = "list key"          # TypeError: unhashable type: 'list'
```

## Common dict patterns

```python
# Safe get with default
d.get("missing_key", "default")

# Iterate key-value pairs
for k, v in d.items(): ...

# Dict comprehension
squares = {x: x**2 for x in range(5)}

# Merge dicts (Python 3.9+)
merged = dict_a | dict_b

# Update in place
dict_a.update(dict_b)
```

## Sets

A set is a dict with only keys (no values). Same hash table, same O(1) lookup.
Use sets for:
- Deduplication
- Membership testing (`if x in my_set` — much faster than `if x in my_list`)
- Set operations: union `|`, intersection `&`, difference `-`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # {1, 2, 3, 4}
print(a & b)   # {2, 3}
print(a - b)   # {1}
```

## Dict ordering

Since Python 3.7, dicts maintain **insertion order**. This is guaranteed
by the language spec — not just an implementation detail.
