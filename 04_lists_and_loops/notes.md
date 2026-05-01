# Lists & Loops — How Iteration Actually Works

## Lists in memory

A list is an array of pointers (references), not the values themselves.
`[1, "hello", [2, 3]]` stores three pointers to three different objects.

This means:
- Lists can hold mixed types (each pointer can point to any object)
- Copying a list only copies the pointers — not the objects they point to (shallow copy)

```python
original = [[1, 2], [3, 4]]
copy = original.copy()
copy[0].append(99)
print(original[0])  # [1, 2, 99] — the inner list is shared!
```

For a true deep copy: `import copy; deep = copy.deepcopy(original)`

## The iterator protocol

Python's `for` loop works on anything that implements the iterator protocol:
- `iter(x)` → returns an iterator object
- `next(iterator)` → returns the next item, raises `StopIteration` when done

```python
nums = [10, 20, 30]
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
next(it)         # raises StopIteration
```

This is exactly what `for n in nums` does under the hood.

## List comprehensions

A concise way to build lists. Equivalent to a loop but faster and more readable:

```python
squares = [x**2 for x in range(10)]

# with a filter
evens = [x for x in range(20) if x % 2 == 0]
```

## zip() and enumerate()

`zip(a, b)` pairs up items from two iterables — stops at the shorter one.

```python
names = ["Alice", "Bob"]
scores = [95, 80]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

`enumerate(x)` wraps an iterable, yielding `(index, value)` pairs.

## Sorting

`sorted()` returns a new sorted list. `.sort()` sorts in place.

```python
words = ["banana", "apple", "cherry"]
print(sorted(words))              # alphabetical
print(sorted(words, key=len))     # by length — key= takes a function
```
