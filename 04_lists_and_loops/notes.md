# Module 4: Lists & Loops

## What is a list?

A list stores multiple values in order. You can change it after creating it (it's mutable). Each item can be any type.

---

## Step 1: Creating and accessing lists

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # first item
print(fruits[-1])   # last item
print(fruits[1:])   # from index 1 to end
print(len(fruits))  # number of items
```

**What you should see:** `apple`, `cherry`, `['banana', 'cherry']`, `3`

Indexes start at 0. Negative indexes count from the end: `-1` is the last item, `-2` is second-to-last.

---

## Step 2: Modifying lists

```python
nums = [3, 1, 4, 1, 5]
nums.append(9)       # add to end
nums.insert(0, 0)    # insert at index 0
nums.remove(1)       # remove first occurrence of 1
popped = nums.pop()  # remove and return last item

print(nums)
print(popped)
```

**Try each line one at a time** — add a `print(nums)` after each operation to see what changes.

---

## Step 3: The shallow copy trap

A list stores **pointers** to objects, not the objects themselves. Copying a list only copies the pointers.

```python
original = [[1, 2], [3, 4]]
copy = original.copy()

copy[0].append(99)

print("original:", original)
print("copy:    ", copy)
```

**What you should see:** Both show `[1, 2, 99]` in the first position — the inner list is shared.

**Fix with deep copy:**

```python
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(99)

print("original:", original)
print("deep:    ", deep)
```

**What you should see:** `original` is untouched.

---

## Step 4: List comprehensions

A list comprehension is a short, clean way to build a list.

**Long way:**
```python
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)
```

**Short way (comprehension):**
```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)
```

**What you should see:** `[1, 4, 9, 16, 25]` — same result, one line.

**With a filter:**
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

**Read it as:** "give me `x` for each `x` in range(10), but only if `x` is even."

---

## Step 5: Sorting

```python
words = ["banana", "fig", "apple", "kiwi", "cherry"]

print(sorted(words))              # new sorted list, alphabetical
print(sorted(words, key=len))     # sorted by length
print(words)                      # original unchanged
```

`sorted()` always returns a **new** list. The original is untouched.

`.sort()` sorts **in place** and returns `None`:

```python
words.sort()
print(words)   # now sorted
```

---

## Step 6: zip and enumerate

`enumerate()` gives you index + value:

```python
animals = ["cat", "dog", "bird"]
for i, animal in enumerate(animals):
    print(f"{i}: {animal}")
```

`zip()` pairs up two lists:

```python
names = ["Alice", "Bob", "Carol"]
scores = [88, 95, 70]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Build a dict from two lists:
score_dict = dict(zip(names, scores))
print(score_dict)
```

---

## Step 7: Useful built-ins for lists

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(min(nums))
print(max(nums))
print(sum(nums))
print(any(x > 8 for x in nums))    # is any number > 8?
print(all(x > 0 for x in nums))    # are all numbers > 0?
```

---

## Now try it yourself

Start with this and modify it:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Challenge 1: Use a comprehension to get only even numbers
evens = []   # replace with a comprehension

# Challenge 2: Get the square of each even number
squares_of_evens = []   # one-line comprehension with a filter

print(evens)
print(squares_of_evens)
```
