# Module 3: Functions

## What is a function?

A function is a reusable block of code. You give it a name, and you can run it any time by calling that name. Functions help you avoid repeating yourself and break complex problems into smaller pieces.

---

## Step 1: Your first function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Jack"))
print(greet("Alice"))
```

**What you should see:**
```
Hello, Jack!
Hello, Alice!
```

- `def` tells Python you're defining a function
- `greet` is the name
- `name` is a **parameter** — a placeholder for whatever you pass in
- `return` sends a value back to whoever called the function

---

## Step 2: Functions are objects

This is what makes Python powerful. A function is just an object — like a list or a string. You can store it in a variable, pass it to another function, put it in a list.

```python
def double(x):
    return x * 2

# Assign to another variable
times_two = double
print(times_two(5))

# Pass as an argument
def apply(func, value):
    return func(value)

print(apply(double, 7))
```

**What you should see:** `10` then `14`

**Why this matters:** This is how `sorted(key=len)` works — you're passing the `len` function as an argument.

---

## Step 3: The mutable default argument trap

This catches everyone. Run this:

```python
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_to_list("a"))
print(add_to_list("b"))
print(add_to_list("c"))
```

**What you should see:**
```
['a']
['a', 'b']
['a', 'b', 'c']
```

**Why?** The `[]` default is created **once** when Python reads the `def` line — not each time you call the function. Every call shares the same list.

**The fix** — use `None` as the default:

```python
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_to_list("a"))
print(add_to_list("b"))
print(add_to_list("c"))
```

**What you should see:** Three separate lists — `['a']`, `['b']`, `['c']`

---

## Step 4: *args — any number of arguments

Put `*` before a parameter name and it collects all extra positional arguments into a **tuple**.

```python
def my_sum(*args):
    total = 0
    for n in args:
        total += n
    return total

print(my_sum(1, 2, 3))
print(my_sum(10, 20))
print(my_sum(1, 2, 3, 4, 5, 6))
```

**What you should see:** `6`, `30`, `21`

---

## Step 5: **kwargs — any number of keyword arguments

Put `**` before a parameter name and it collects all extra keyword arguments into a **dict**.

```python
def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

describe(name="Jack", role="founder", age=28)
```

**What you should see:**
```
name = Jack
role = founder
age = 28
```

---

## Step 6: Scope — where Python looks for names

When Python sees a name, it searches in this order: **Local → Enclosing → Global → Built-in** (LEGB).

```python
x = "I am global"

def outer():
    x = "I am enclosing"
    def inner():
        print(x)   # finds "enclosing" before "global"
    inner()

outer()
print(x)   # global x is unchanged
```

**What you should see:** `I am enclosing` then `I am global`

---

## Step 7: Closures — functions that remember

A closure is a function that **remembers** the variables from where it was created, even after the outer function has finished.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n   # `n` is captured from the outer function
    return multiplier

triple = make_multiplier(3)
double = make_multiplier(2)

print(triple(10))   # 30
print(triple(7))    # 21
print(double(5))    # 10
```

**What you should see:** `30`, `21`, `10`

Each call to `make_multiplier` creates a brand new function with its own captured `n`. `triple` and `double` are completely independent.

---

## Now try it yourself

Write a function called `make_adder(n)` that returns a function which adds `n` to its argument:

```python
add5 = make_adder(5)
print(add5(10))   # should print 15
print(add5(3))    # should print 8
```
