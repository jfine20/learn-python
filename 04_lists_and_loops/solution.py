# Module 04 — Solutions
import copy

# ── Exercise 1 ────────────────────────────────────────────────────────────────
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0].append(99)
print(original[0])  # [1, 2, 99] — the inner list is SHARED
print(shallow[0])   # [1, 2, 99]
# .copy() duplicates the outer list but the pointers inside still point to the same inner lists.

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(99)
print(original[0])  # [1, 2] — untouched

# ── Exercise 2 ────────────────────────────────────────────────────────────────
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
try:
    next(it)
except StopIteration:
    print("Iterator exhausted — no more items")

# ── Exercise 3 ────────────────────────────────────────────────────────────────
squares = [x**2 for x in range(1, 11)]
print(squares)

long_words = [w for w in ["hi", "hello", "world", "python", "ok"] if len(w) > 4]
print(long_words)

pairs = [(x, x**2) for x in range(1, 6)]
print(pairs)

# ── Exercise 4 ────────────────────────────────────────────────────────────────
names = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 70]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

score_dict = dict(zip(names, scores))
print(score_dict)

# ── Exercise 5 ────────────────────────────────────────────────────────────────
words = ["banana", "fig", "apple", "kiwi", "cherry"]
print(sorted(words))                          # alphabetical
print(sorted(words, key=len))                 # by length
print(sorted(words, key=lambda w: (len(w), w)))  # length, then alpha for ties

# ── Exercise 6 ────────────────────────────────────────────────────────────────
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Read it as: "for each sublist in nested, for each item in sublist, give me item"
