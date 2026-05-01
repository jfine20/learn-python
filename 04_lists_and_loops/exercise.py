# Module 04 — Lists & Loops
# Run: python 04_lists_and_loops/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Shallow copy gotcha.
original = [[1, 2], [3, 4]]
copy = original.copy()
copy[0].append(99)
# TODO: print both original[0] and copy[0]. Explain in a comment WHY they're the same.
# Then fix it using copy.deepcopy().


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# The iterator protocol manually.
numbers = [10, 20, 30]
# TODO: get an iterator from numbers using iter().
# Then call next() 3 times. Then call next() a 4th time and catch the StopIteration.


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# List comprehensions.
# TODO: using a list comprehension (single line), create:
#   a) squares of numbers 1-10
#   b) all words longer than 4 chars from: ["hi", "hello", "world", "python", "ok"]
#   c) a list of (number, square) tuples for 1-5


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# zip() — pair up two lists.
names = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 70]
# TODO: use zip to print "Alice scored 88", etc.
# Then use zip to create a dict: {"Alice": 88, ...} in one line.


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# Sorting with a key function.
words = ["banana", "fig", "apple", "kiwi", "cherry"]
# TODO:
#   a) sort alphabetically
#   b) sort by length
#   c) sort by length, then alphabetically for ties (hint: key can return a tuple)


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# Flatten a nested list using a list comprehension.
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# TODO: create `flat` = [1, 2, 3, 4, 5, 6, 7, 8, 9] using a comprehension.
# Hint: you can nest two `for` clauses in one comprehension.
