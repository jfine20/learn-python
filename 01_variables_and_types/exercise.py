# Module 01 — Variables & Types
# Run this file: python 01_variables_and_types/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Predict what this prints BEFORE running it. Then run it. Were you right?

a = [1, 2, 3]
b = a
a.append(99)
# TODO: what does b equal here? Write your prediction as a comment, then print b.


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# How do you make a TRUE copy of a list so that changes to one don't affect the other?
# TODO: create a copy of `a` called `c`, then append 999 to `a`.
# Verify that `c` is unchanged.


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# id() returns the memory address of an object.
# TODO: print id(a) and id(b). Are they the same?
# Now print id(a) and id(c). Are they the same?


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# Strings are immutable. Prove it.
# TODO: create s = "hello". Try s[0] = "H". What happens and why?
# (wrap it in try/except to catch the error and print a message explaining it)


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# Python reuses small integer objects (a quirk called "integer interning").
# TODO: check if `x = 5` and `y = 5` share the same id. Do they?
# Now try with x = 1000, y = 1000. Do they?
# What does this tell you about how Python manages memory?


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# TODO: write a function called `what_type` that takes any value and prints:
#   "Value: <value>, Type: <type>, Mutable: yes/no"
# Call it with: 42, "hello", [1,2,3], (1,2,3), {"key": "val"}, None

def what_type(value):
    pass  # replace this
