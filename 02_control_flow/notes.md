# Module 2: Control Flow

## What is control flow?

So far your programs have run top to bottom, every line, every time. **Control flow** is how you change that — making decisions, skipping code, and repeating things.

This is where programs start to feel alive.

---

## Step 1: if / elif / else

The basics. Type this and run it:

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

**What you should see:** `B`

Try changing `score` to different numbers and re-running. Notice: Python checks conditions **top to bottom** and stops at the first true one.

---

## Step 2: Truthiness — Python doesn't need == True

In Python, every object has a truth value. You don't need `if x == True` — you can just write `if x`.

**Falsy** (treated as False): `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`

**Truthy**: everything else — including `"0"`, `[0]`, `-1`

Try this:

```python
values = [0, 1, "", "hello", [], [0], None, {"key": "val"}]

for v in values:
    if v:
        print(f"{repr(v):20} → truthy")
    else:
        print(f"{repr(v):20} → falsy")
```

**What you should see:** Each value labelled truthy or falsy.

**Why this matters:** Instead of `if len(my_list) > 0:` you just write `if my_list:` — cleaner and more Pythonic.

---

## Step 3: and / or return values, not True/False

This surprises people. `and` and `or` don't return `True` or `False` — they return one of their operands.

Try this:

```python
print(None or "fallback")
print("real" or "fallback")
print(0 and "never reached")
print(1 and "this gets returned")
```

**What you should see:**
```
fallback
real
0
this gets returned
```

**The rule:**
- `or` returns the **first truthy** value, or the last value if all are falsy
- `and` returns the **first falsy** value, or the last value if all are truthy

**Real world use:** Setting defaults safely:

```python
username = None
display_name = username or "Anonymous"
print(display_name)
```

---

## Step 4: for loops — not about indexes

Python's `for` loop doesn't count indexes like `for (i=0; i<n; i++)`. It says **"give me the next item"** and works on anything that can produce items.

```python
for item in [10, 20, 30]:
    print(item)
```

```python
for char in "Python":
    print(char)
```

```python
for key in {"name": "Jack", "age": 28}:
    print(key)
```

**Try all three.** Notice: looping over a dict gives you the keys.

---

## Step 5: enumerate and zip

When you need the index too, use `enumerate()`:

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

When you want to loop two lists at once, use `zip()`:

```python
names = ["Alice", "Bob", "Carol"]
scores = [95, 80, 88]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

---

## Step 6: range() is lazy

`range(1000000)` does NOT make a list of a million numbers. It's an object that generates numbers one at a time on demand.

```python
r = range(10)
print(type(r))
print(r[4])
print(list(r))
```

**What you should see:** It's a `range` object. You can index it directly. Only when you call `list()` does it generate all values.

---

## Step 7: FizzBuzz — put it together

Classic exercise. Print numbers 1–20. Replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".

The `%` operator gives you the **remainder** after division: `9 % 3 == 0` means 9 is divisible by 3.

```python
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```

**Try modifying it:** Can you make it go to 100? Can you add a rule for multiples of 7 printing "Jazz"?

---

## Step 8: break and continue

```python
for n in range(10):
    if n == 3:
        continue    # skip the rest of this iteration
    if n == 7:
        break       # exit the loop entirely
    print(n)
```

**What you should see:** 0, 1, 2, 4, 5, 6 — 3 is skipped, loop stops before 7.
