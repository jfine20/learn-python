# Control Flow — How Python Decides What's True

## Truthiness vs. equality

Python doesn't need `== True`. Every object has a truth value.

**Falsy** (treated as False in a boolean context):
- `None`
- `0`, `0.0`
- `""` (empty string)
- `[]`, `{}`, `set()`, `()` (empty collections)
- Any object whose `__bool__` returns False

**Everything else is truthy.**

```python
items = []
if items:          # asks "does this list have anything?" — clean Python
    print("has items")

if len(items) > 0: # also correct, but wordy
    print("has items")
```

## Short-circuit evaluation

`and` and `or` don't return True/False — they return one of their operands.

```python
x = None
name = x or "default"   # if x is falsy, use "default"
print(name)             # "default"

user = {"admin": True}
is_admin = user and user["admin"]  # safe — won't crash if user is None/{}
```

`and` returns the first falsy value, or the last value if all are truthy.
`or` returns the first truthy value, or the last value if all are falsy.

## for loops are about iterables, not indexes

Python's `for` loop doesn't say "give me index 0, 1, 2...". It says
"give me the next item" — it works on anything *iterable*.

```python
for char in "hello":   # strings are iterable
    print(char)

for key in {"a": 1}:  # dicts iterate over keys
    print(key)
```

Under the hood, `for x in thing` calls `iter(thing)` to get an iterator,
then calls `next()` on it repeatedly until `StopIteration` is raised.

## range() is lazy

`range(1000000)` does NOT create a list of a million numbers. It creates a
range object that generates numbers on demand. This is why it's fast and
uses almost no memory.

```python
r = range(10)
print(type(r))   # <class 'range'>
print(list(r))   # NOW it creates the list
```

## while vs for

Use `for` when you know what you're iterating over.
Use `while` when you're waiting for a condition to change.

```python
# Good use of while
response = None
while response != "quit":
    response = input("> ")
```
