print("=" * 50)
print("MODULE 4: Lists & Loops")
print("=" * 50)

import copy

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: Lists store pointers, not values ---")
# ─────────────────────────────────────────────────

# A list doesn't store the actual objects. It stores POINTERS to objects.
# [1, "hello", [2,3]] → three pointers to three different objects in memory.
# This means: copying a list only copies the pointers, not the objects.

print("Shallow copy trap:")
original = [[1, 2], [3, 4]]
shallow  = original.copy()

shallow[0].append(99)   # modifies the inner list — which BOTH lists point to

print(f"  original = {original}")   # [[1, 2, 99], [3, 4]]  ← affected!
print(f"  shallow  = {shallow}")    # [[1, 2, 99], [3, 4]]

print("\nFix: deep copy duplicates everything, all the way down:")
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(99)
print(f"  original = {original}")   # [[1, 2], [3, 4]]  ← untouched
print(f"  deep     = {deep}")       # [[1, 2, 99], [3, 4]]

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: The iterator protocol — what for loops actually do ---")
# ─────────────────────────────────────────────────

# for x in thing: is shorthand for:
#   it = iter(thing)   → get an iterator
#   while True:
#       x = next(it)   → get next item
#       ...            → if StopIteration is raised, stop

print("Manually doing what `for` does internally:")
nums = [10, 20, 30]
it = iter(nums)
print(f"  next(it) = {next(it)}")   # 10
print(f"  next(it) = {next(it)}")   # 20
print(f"  next(it) = {next(it)}")   # 30
try:
    next(it)
except StopIteration:
    print("  StopIteration raised — iterator is exhausted")

print("\nThis works on anything iterable — strings, dicts, files, ranges...")
it = iter("hi")
print(f"  next(iter('hi')) = '{next(it)}'")
print(f"  next(iter('hi')) = '{next(it)}'")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: List comprehensions ---")
# ─────────────────────────────────────────────────

# A compact, readable way to build a list.
# [expression  for item in iterable  if condition]

print("Loop version vs comprehension version:")

squares_loop = []
for x in range(1, 6):
    squares_loop.append(x ** 2)

squares_comp = [x ** 2 for x in range(1, 6)]

print(f"  loop:          {squares_loop}")
print(f"  comprehension: {squares_comp}")

print("\nWith a filter (the if at the end):")
evens = [x for x in range(10) if x % 2 == 0]
print(f"  evens: {evens}")

print("\nNested: flatten a 2D list:")
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in nested for item in row]
print(f"  flat: {flat}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: Useful list tools ---")
# ─────────────────────────────────────────────────

words = ["banana", "fig", "apple", "kiwi", "cherry"]

print("sorted() — returns a new sorted list, original unchanged:")
print(f"  alphabetical: {sorted(words)}")
print(f"  by length:    {sorted(words, key=len)}")
print(f"  original:     {words}")   # unchanged

print("\n.sort() — sorts IN PLACE, returns None:")
words.sort()
print(f"  after .sort(): {words}")

print("\nmin(), max(), sum() work on any iterable:")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"  nums = {nums}")
print(f"  min={min(nums)}, max={max(nums)}, sum={sum(nums)}")

print("\nany() and all():")
print(f"  any([False, False, True]) = {any([False, False, True])}")
print(f"  all([True, True, True])   = {all([True, True, True])}")
print(f"  all([True, False, True])  = {all([True, False, True])}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Add your code below. Save and run after each one.

1. Using a list comprehension, create a list of all numbers 1-50
   that are divisible by 3 OR divisible by 7.

2. You have two lists:
     names  = ["Alice", "Bob", "Carol"]
     scores = [88, 95, 70]
   Use zip() and a dict comprehension to make: {"Alice": 88, "Bob": 95, "Carol": 70}

3. Given this nested list, use a comprehension to get just the first element of each:
     data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
   Expected result: [10, 40, 70]
""")

# YOUR CODE HERE ↓
