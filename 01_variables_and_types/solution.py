# Module 01 — Solutions

# ── Exercise 1 ────────────────────────────────────────────────────────────────
a = [1, 2, 3]
b = a
a.append(99)
print(b)  # [1, 2, 3, 99]
# b and a are two names for the SAME list object. Appending to a mutates the
# underlying object, so b "sees" the change.

# ── Exercise 2 ────────────────────────────────────────────────────────────────
# Three ways to make a shallow copy:
c = a.copy()      # most explicit
c = a[:]          # slice copy — idiomatic but less readable
c = list(a)       # construct a new list from the iterable

a.append(999)
print(c)  # unchanged — c points to a different list object

# ── Exercise 3 ────────────────────────────────────────────────────────────────
print(id(a) == id(b))  # True — same object
print(id(a) == id(c))  # False — different objects

# ── Exercise 4 ────────────────────────────────────────────────────────────────
s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print(f"Can't do that: {e}")
# str is immutable — no method or index assignment can change the characters.
# s = "Hello" would work, but that creates a NEW string and rebinds the name s.

# ── Exercise 5 ────────────────────────────────────────────────────────────────
x = 5
y = 5
print(id(x) == id(y))   # True — Python caches ints -5 to 256

x = 1000
y = 1000
print(id(x) == id(y))   # False (usually) — large ints are not interned
# Takeaway: never use `is` to compare integers. Use `==`. `is` tests identity
# (same object), `==` tests equality (same value). They are not the same thing.

# ── Exercise 6 ────────────────────────────────────────────────────────────────
MUTABLE_TYPES = (list, dict, set)

def what_type(value):
    mutable = "yes" if isinstance(value, MUTABLE_TYPES) else "no"
    print(f"Value: {value!r}, Type: {type(value).__name__}, Mutable: {mutable}")

what_type(42)
what_type("hello")
what_type([1, 2, 3])
what_type((1, 2, 3))
what_type({"key": "val"})
what_type(None)
