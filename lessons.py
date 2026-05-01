LESSONS = [
    {
        "id": "00_the_basics",
        "title": "The Basics",
        "steps": [
            {
                "title": "What is code?",
                "teach": """## What is code?

Code is just **instructions you write for a computer**. The computer reads them top to bottom and does exactly what you say — nothing more, nothing less.

Python is the language you're learning. It's one of the most readable programming languages — it looks almost like English.

The most important thing in Python is `print()` — it displays something on the screen.

**Try it:** The code on the right is already loaded. Hit **Run** and see what happens.

Then try changing `Hello, world!` to your name and run it again.""",
                "code": 'print("Hello, world!")',
                "expected": "Hello, world!",
                "hint": "Make sure your text is inside quotes, and inside parentheses: print(\"your text\")",
            },
            {
                "title": "Comments",
                "teach": """## Comments — notes for humans, ignored by Python

A **comment** starts with `#`. Python completely ignores anything after `#` on a line.

Use comments to leave notes explaining what your code does.

```python
# This is a comment
print("This runs")  # This comment is ignored
```

**Run the code on the right.** Notice that the comment lines don't appear in the output — only the `print()` lines do.

Comments are important. When you come back to code you wrote weeks ago, good comments remind you what you were thinking.""",
                "code": """# I am a comment — Python ignores me
print("But this prints!")

# You can put comments anywhere
print("Hello")  # even at the end of a line
""",
                "expected": "But this prints!\nHello",
                "hint": "Comments start with #. Everything after # on that line is ignored.",
            },
            {
                "title": "Math",
                "teach": """## Python as a calculator

Python can do math. Run the code and look at each result.

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | add | `3 + 2` = 5 |
| `-` | subtract | `3 - 2` = 1 |
| `*` | multiply | `3 * 2` = 6 |
| `/` | divide | `7 / 2` = 3.5 |
| `//` | floor divide (drop decimal) | `7 // 2` = 3 |
| `%` | remainder (modulo) | `7 % 2` = 1 |
| `**` | power (exponent) | `3 ** 2` = 9 |

The `%` operator is especially useful. `7 % 2` asks: "what's left over after dividing 7 by 2?" The answer is 1 because 7 = 3×2 + 1.

**After running, try:** change the numbers and predict the result before running again.""",
                "code": """print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 8)
""",
                "expected": "13\n7\n30\n3.3333333333333335\n3\n1\n256",
                "hint": "Just run it and look at each number. 10 % 3 is 1 because 10 = 3×3 + 1.",
            },
            {
                "title": "Variables",
                "teach": """## Variables — storing values

A **variable** stores a value so you can use it later and give it a name.

```python
name = "Jack"
age = 28
```

Read `=` as **"gets"** — not "equals". So `name = "Jack"` means "name **gets** the value Jack".

Once stored, you can use the variable anywhere:

```python
print(name)
print(age + 10)
```

**Try it:** Run the code, then change the price and see how the total updates automatically. This is the power of variables — you change one thing and everything that uses it updates.""",
                "code": """price = 100
tax_rate = 0.08

tax = price * tax_rate
total = price + tax

print(price)
print(tax)
print(total)
""",
                "expected": "100\n8.0\n108.0",
                "hint": "Variables let you store values with names. Change price = 100 to price = 200 and re-run.",
            },
            {
                "title": "Strings",
                "teach": """## Strings — working with text

A **string** is text. Wrap it in quotes (single or double — both work).

```python
"hello"   # double quotes
'hello'   # single quotes — same thing
```

**Joining strings** (called concatenation):
```python
first = "Jack"
last = "Fine"
full = first + " " + last   # "Jack Fine"
```

**f-strings** — the best way to mix variables into text:
```python
name = "Jack"
age = 28
print(f"My name is {name} and I am {age} years old.")
```

The `f` before the quote tells Python: look for `{}` and replace what's inside with the variable's value.

**Run the code and then change the name and age to your own.**""",
                "code": """name = "Jack"
age = 28
city = "New York"

print(f"Hi, I'm {name}.")
print(f"I'm {age} years old and I live in {city}.")
print(f"In 10 years I'll be {age + 10}.")
""",
                "expected": "Hi, I'm Jack.\nI'm 28 years old and I live in New York.\nIn 10 years I'll be 38.",
                "hint": "f-strings use {} to insert variables. The f goes right before the opening quote.",
            },
            {
                "title": "Indentation",
                "teach": """## Indentation — Python's biggest rule

In Python, **indentation (spaces at the start of a line) controls which code belongs together**.

```python
if 5 > 3:
    print("this is indented")   # belongs to the if
    print("so is this")         # belongs to the if
print("this always runs")       # NOT indented — outside the if
```

Use **4 spaces** per level. The Tab key inserts 4 spaces automatically in this editor.

Get indentation wrong and you get an `IndentationError`. Python is very picky about this.

**Run the code.** Then try removing the spaces before one of the indented print lines and run again — see the error you get. This is one of the most common beginner mistakes.""",
                "code": """score = 85

if score >= 90:
    print("You got an A!")
    print("Great work.")
elif score >= 80:
    print("You got a B!")
else:
    print("Keep practicing.")

print("Done checking score.")
""",
                "expected": "You got a B!\nDone checking score.",
                "hint": "Each line inside an if/elif/else must be indented with 4 spaces. The last print is NOT indented so it always runs.",
            },
            {
                "title": "Reading errors",
                "teach": """## Errors are normal — learn to read them

Every programmer sees errors constantly. When you get one, read it **bottom to top**:

1. The **last line** tells you the type of error and what went wrong
2. The line above tells you where it happened

**Common errors:**
- `SyntaxError` — Python can't understand what you wrote (typo, missing bracket)
- `NameError` — you used a variable that doesn't exist yet
- `TypeError` — wrong type (e.g., adding a number to text without converting)
- `IndentationError` — your spacing is wrong

**Try running the code** — it has a bug. Read the error message. Then fix it and run again.

Hint: look at the print statement carefully.""",
                "code": """name = "Jack"
age = 28

print("Name: " + name)
print("Age: " + age)
""",
                "expected": "Name: Jack\nAge: 28",
                "hint": "You can't add a string and a number with +. Convert age to a string first: str(age). Or use an f-string instead: f\"Age: {age}\"",
            },
        ],
    },
    {
        "id": "01_variables_and_types",
        "title": "Variables & Types",
        "steps": [
            {
                "title": "Variables are name tags, not boxes",
                "teach": """## Variables are name tags, not boxes

Most people picture a variable as a **box** you put a value into. In Python, that's wrong — and it leads to bugs.

Think of a variable as a **name tag** you stick on an object. The object exists in memory. The name tag just points to it.

When you write `b = a`, you're not copying the list. You're sticking a second name tag on the **same** list.

**Run the code and look at the output.** Both `a` and `b` show the same thing — because they're pointing to the same list in memory.

Does this surprise you? This is one of Python's most important concepts.""",
                "code": """a = [1, 2, 3]
b = a          # b is a second name tag for the SAME list

a.append(99)   # change the list through a

print("a =", a)
print("b =", b)
print("Same object?", id(a) == id(b))
""",
                "expected": "a = [1, 2, 3, 99]\nb = [1, 2, 3, 99]\nSame object? True",
                "hint": "id() shows the memory address of an object. If id(a) == id(b), they ARE the same object — not copies.",
            },
            {
                "title": "Making a real copy",
                "teach": """## Making a real copy

Since `b = a` makes another name tag (not a copy), how do you make a real, independent copy?

Use `.copy()`:
```python
b = a.copy()   # now b is a NEW list with the same values
```

After this, `a` and `b` are completely independent. Changing one doesn't affect the other.

**Run the code** and see the difference. Then try changing `a.copy()` back to just `a` and see how the output changes.""",
                "code": """a = [1, 2, 3]
b = a.copy()   # a REAL copy — different object

a.append(99)

print("a =", a)
print("b =", b)
print("Same object?", id(a) == id(b))
""",
                "expected": "a = [1, 2, 3, 99]\nb = [1, 2, 3]\nSame object? False",
                "hint": "Try changing b = a.copy() to just b = a and re-run. Watch what happens to b.",
            },
            {
                "title": "Mutable vs Immutable",
                "teach": """## Mutable vs Immutable

**Mutable** means the object can be changed after it's created.
**Immutable** means it can never be changed.

- **Immutable:** `int`, `float`, `str`, `bool`, `tuple`
- **Mutable:** `list`, `dict`, `set`

**Strings are immutable.** When you do `s = s + " world"`, Python doesn't change the original string. It creates a brand new string and points `s` at it.

**Run the code** and notice: the `id` changes after reassigning `s`. It's a completely different object in memory. The original `"hello"` was never touched.""",
                "code": """s = "hello"
print("before:", s, "  id:", id(s))

s = s + " world"
print("after: ", s, "  id:", id(s))

print("id changed?", True)
print()

# Lists ARE mutable — same object, modified
lst = [1, 2, 3]
print("before:", lst, "  id:", id(lst))
lst.append(4)
print("after: ", lst, "  id:", id(lst))
print("id changed?", False)
""",
                "expected": None,
                "hint": "Watch the id numbers. For strings, the id changes — new object. For lists, the id stays the same — same object was modified.",
            },
            {
                "title": "Types",
                "teach": """## Types — every object has one

Every value in Python has a **type** — what kind of thing it is.

| Type | Example | What it is |
|------|---------|-----------|
| `int` | `42` | whole number |
| `float` | `3.14` | decimal number |
| `str` | `"hello"` | text |
| `bool` | `True` / `False` | yes or no |
| `list` | `[1, 2, 3]` | ordered collection |
| `dict` | `{"key": "val"}` | key-value pairs |
| `NoneType` | `None` | nothing |

Use `type()` to check what type something is.

**Run the code** and see each type. Notice: the variable itself has no type — only the object it points to does. That's why you can reassign `x` from an int to a string.""",
                "code": """print(type(42))
print(type(3.14))
print(type("hello"))
print(type(True))
print(type([1, 2, 3]))
print(type({"key": "val"}))
print(type(None))
print()

x = 42
print(type(x))
x = "now a string"
print(type(x))
""",
                "expected": None,
                "hint": "type() shows what kind of object something is. You can also use isinstance(42, int) which returns True or False.",
            },
            {
                "title": "None",
                "teach": """## None — the absence of a value

`None` is Python's way of saying "nothing" or "no value here." It's not zero. It's not an empty string. It's nothing at all.

You'll see `None` a lot:
- A function that doesn't return anything returns `None`
- Variables before they're set are often `None`
- Dictionary lookups for missing keys can return `None`

**Always use `is None` to check for None** — not `== None`. There's only one `None` object in all of Python, so checking identity (`is`) is the right tool.

**Run the code** and look at what happens when a function doesn't return anything.""",
                "code": """result = None
print(result)
print(type(result))

if result is None:
    print("result is nothing")

# Functions that don't return anything return None
def do_something():
    x = 1 + 1
    # no return statement

value = do_something()
print("returned:", value)
""",
                "expected": "None\n<class 'NoneType'>\nresult is nothing\nreturned: None",
                "hint": "Use 'is None' not '== None'. None is a singleton — there's only one of it in all of Python.",
            },
        ],
    },
    {
        "id": "02_control_flow",
        "title": "Control Flow",
        "steps": [
            {
                "title": "if / elif / else",
                "teach": """## Making decisions with if

So far your code runs every line, every time. `if` lets you **skip** lines based on a condition.

```python
if condition:
    # runs only if condition is True
elif other_condition:
    # runs if first was False, this is True
else:
    # runs if everything above was False
```

Python checks conditions **top to bottom** and stops at the first true one.

**Run the code.** Then change `score` to 95, then 72, then 50 — run after each change and see which branch executes.""",
                "code": """score = 85

if score >= 90:
    print("A — excellent!")
elif score >= 80:
    print("B — good job!")
elif score >= 70:
    print("C — passing")
else:
    print("Below passing — keep practicing")

print("Score was:", score)
""",
                "expected": "B — good job!\nScore was: 85",
                "hint": "Try score = 95 (gets A), score = 72 (gets C), score = 50 (gets the else). Only ONE branch runs.",
            },
            {
                "title": "Truthiness",
                "teach": """## Truthiness — Python doesn't need == True

In Python, `if x:` doesn't require `x` to literally be `True`. Python evaluates the **truthiness** of `x`.

**Falsy** (treated as False): `0`, `""`, `[]`, `{}`, `None`
**Truthy**: everything else — `1`, `"hi"`, `[0]`, `{"a": 1}`

This means instead of:
```python
if len(my_list) > 0:
```
You can just write:
```python
if my_list:
```

**Run the code** and look at which values are falsy. Some might surprise you — like `[0]` being truthy (it's a list with something in it, so it's not empty).""",
                "code": """values = [0, 1, "", "hello", [], [0], None, {"key": "val"}]

for v in values:
    if v:
        print(str(v).ljust(15), "truthy")
    else:
        print(str(v).ljust(15), "falsy")
""",
                "expected": None,
                "hint": "The key insight: empty things (0, \"\", [], {}, None) are falsy. Anything with content is truthy — even [0] because the list isn't empty.",
            },
            {
                "title": "and / or",
                "teach": """## and / or — combining conditions

`and` — both sides must be true:
```python
if age >= 18 and has_id:
    print("can enter")
```

`or` — at least one side must be true:
```python
if is_admin or is_owner:
    print("has access")
```

**Surprising fact:** `and` and `or` don't return `True` or `False` — they return one of their operands.

- `or` returns the **first truthy** value (or the last value if all are falsy)
- `and` returns the **first falsy** value (or the last value if all are truthy)

This makes `or` useful as a default: `name = username or "Anonymous"`

**Run the code** and see what each one returns.""",
                "code": """print(None or "fallback")       # None is falsy, so returns "fallback"
print("real" or "fallback")    # "real" is truthy, stops here
print(0 and "nope")            # 0 is falsy, stops here, returns 0
print(1 and "yes")             # 1 is truthy, returns the right side

# Real use case — safe default
username = None
display = username or "Anonymous"
print(display)
""",
                "expected": "fallback\nreal\n0\nyes\nAnonymous",
                "hint": "or returns the first truthy thing it finds. and returns the first falsy thing. If it finds none, it returns the last value.",
            },
            {
                "title": "for loops",
                "teach": """## for loops — doing something for each item

A `for` loop goes through a list (or anything iterable) and runs your code once for each item.

```python
for item in my_list:
    print(item)
```

Think of it as: "**for** each **item** in my_list, do this."

Python's `for` loop doesn't use indexes like many languages. It just asks "give me the next item" — which works on lists, strings, dicts, ranges, anything.

**Run the code.** Then add more names to the list and run again.""",
                "code": """names = ["Alice", "Bob", "Carol", "Dave"]

for name in names:
    print(f"Hello, {name}!")

print()

# Loops work on strings too — each character
for letter in "Python":
    print(letter)
""",
                "expected": "Hello, Alice!\nHello, Bob!\nHello, Carol!\nHello, Dave!\n\nP\ny\nt\nh\no\nn",
                "hint": "The variable after 'for' (name, letter) gets each item one at a time. You can name it anything.",
            },
            {
                "title": "range()",
                "teach": """## range() — counting loops

When you want to repeat something a set number of times, use `range()`:

```python
for i in range(5):
    print(i)   # prints 0, 1, 2, 3, 4
```

`range()` starts at 0 by default. You can customize it:
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(0, 10, 2)` → 0, 2, 4, 6, 8 (step by 2)

**Important:** `range(5)` does NOT create a list of 5 numbers. It's a lazy object that generates one number at a time. That's why `range(1000000)` is instant and uses almost no memory.

**Run the code,** then try changing the range arguments.""",
                "code": """for i in range(5):
    print(i)

print()

for i in range(1, 6):
    print(i)

print()

for i in range(0, 20, 3):
    print(i)
""",
                "expected": "0\n1\n2\n3\n4\n\n1\n2\n3\n4\n5\n\n0\n3\n6\n9\n12\n15\n18",
                "hint": "range(start, stop, step). Stop is exclusive — range(1, 6) goes 1,2,3,4,5 — it stops BEFORE 6.",
            },
            {
                "title": "FizzBuzz challenge",
                "teach": """## FizzBuzz — your first real challenge

FizzBuzz is a classic programming exercise. The rules:

- Print numbers 1 to 20
- If a number is divisible by 3, print "Fizz" instead
- If divisible by 5, print "Buzz" instead
- If divisible by both 3 and 5, print "FizzBuzz" instead

**The `%` operator gives you the remainder:**
- `9 % 3 == 0` means 9 is divisible by 3 (no remainder)
- `10 % 5 == 0` means 10 is divisible by 5

**Important:** check for "both 3 and 5" FIRST — otherwise the code will never reach it.

**Write the solution yourself.** The structure is already there — fill in the conditions.""",
                "code": """for n in range(1, 21):
    if n % 15 == 0:       # divisible by both 3 and 5
        print("FizzBuzz")
    elif n % 3 == 0:      # divisible by 3
        print("Fizz")
    elif n % 5 == 0:      # divisible by 5
        print("Buzz")
    else:
        print(n)
""",
                "expected": "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz",
                "hint": "Check n % 15 == 0 FIRST (both), then n % 3 == 0, then n % 5 == 0. Order matters!",
            },
        ],
    },
    {
        "id": "03_functions",
        "title": "Functions",
        "steps": [
            {
                "title": "What is a function?",
                "teach": """## Functions — reusable blocks of code

A function is a named block of code you can run whenever you want by "calling" it.

```python
def function_name(parameter):
    # code here
    return result
```

- `def` — tells Python you're defining a function
- `function_name` — the name you'll use to call it
- `parameter` — a value you pass in (the input)
- `return` — sends a value back out (the output)

Without `return`, a function returns `None`.

**Run the code.** Then try calling `greet()` with different names.""",
                "code": """def greet(name):
    return f"Hello, {name}! Welcome to Python."

print(greet("Jack"))
print(greet("Alice"))
print(greet("everyone"))
""",
                "expected": "Hello, Jack! Welcome to Python.\nHello, Alice! Welcome to Python.\nHello, everyone! Welcome to Python.",
                "hint": "Call a function by writing its name followed by parentheses with the argument inside: greet(\"your name\")",
            },
            {
                "title": "Parameters and return values",
                "teach": """## Parameters and return values

Functions can take multiple parameters and return calculated values.

```python
def add(a, b):
    return a + b

result = add(3, 5)   # result = 8
```

The `return` value can be stored in a variable or used directly:

```python
print(add(3, 5))        # use directly
total = add(10, 20)     # store in variable
```

**Run the code.** Then write your own function at the bottom that calculates the area of a rectangle (width × height).""",
                "code": """def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

print(add(3, 5))
print(multiply(4, 6))
print(is_even(10))
print(is_even(7))

# What does this return?
result = add(10, multiply(2, 3))
print(result)
""",
                "expected": "8\n24\nTrue\nFalse\n16",
                "hint": "add(10, multiply(2, 3)) → multiply(2,3)=6 first, then add(10, 6)=16. Functions can be nested.",
            },
            {
                "title": "Default parameters",
                "teach": """## Default parameters

You can give parameters a default value — used when the caller doesn't provide one.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

Now you can call it two ways:
```python
greet("Jack")            # uses default: "Hello, Jack!"
greet("Jack", "Hey")     # overrides default: "Hey, Jack!"
```

**⚠️ The trap:** Never use a mutable object (like a list) as a default value. It's created ONCE and shared across all calls.

**Run the code** and see the bug, then see the fix.""",
                "code": """# THE BUG — list default is shared across all calls
def broken(item, my_list=[]):
    my_list.append(item)
    return my_list

print(broken("a"))
print(broken("b"))    # surprise!
print(broken("c"))    # worse!

print()

# THE FIX — use None as default
def fixed(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(fixed("a"))
print(fixed("b"))    # fresh list
print(fixed("c"))    # fresh list
""",
                "expected": "['a']\n['a', 'b']\n['a', 'b', 'c']\n\n['a']\n['b']\n['c']",
                "hint": "The [] default is created when Python reads the def line — once, forever. Every call shares it. Use None instead and create a new list inside the function.",
            },
            {
                "title": "Functions are objects",
                "teach": """## Functions are objects

In Python, a function is just an object — like a list or a string. You can store it in a variable and pass it to another function.

This lets you write functions that take OTHER functions as arguments:

```python
def apply(func, value):
    return func(value)

apply(double, 5)   # passes the double function itself
```

This is how `sorted(key=len)` works — you're passing the `len` function as an argument to `sorted`.

**Run the code** and then try passing `str.upper` instead of `len` to `sorted`.""",
                "code": """def double(x):
    return x * 2

def square(x):
    return x ** 2

# Pass functions as arguments
def apply(func, value):
    return func(value)

print(apply(double, 5))
print(apply(square, 4))

# sorted() takes a function as the key=
words = ["banana", "fig", "apple", "kiwi"]
print(sorted(words, key=len))   # sorted by length
""",
                "expected": "10\n16\n['fig', 'kiwi', 'apple', 'banana']",
                "hint": "When you write double without parentheses, you're referring to the function object itself. With parentheses double(5), you're calling it.",
            },
            {
                "title": "Closures",
                "teach": """## Closures — functions that remember

A closure is a function created inside another function, that **remembers** the variables from where it was created — even after the outer function has finished.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n   # remembers n
    return multiplier
```

When you call `make_multiplier(3)`, it returns a new function that always multiplies by 3. The `n=3` is "captured" inside.

**Run the code.** Notice that `triple` and `double` are completely independent — each has its own captured `n`.""",
                "code": """def make_multiplier(n):
    def multiplier(x):
        return x * n   # n is captured from the outer function
    return multiplier

triple = make_multiplier(3)
double = make_multiplier(2)

print(triple(10))    # 30
print(triple(7))     # 21
print(double(5))     # 10
print(double(100))   # 200

# YOUR TURN: write make_adder(n) that returns a function which adds n
def make_adder(n):
    pass   # replace this

add5 = make_adder(5)
# print(add5(10))   # should print 15 — uncomment to test
""",
                "expected": "30\n21\n10\n200",
                "hint": "make_adder should look just like make_multiplier but use + instead of *. The inner function captures n.",
            },
        ],
    },
    {
        "id": "04_lists_and_loops",
        "title": "Lists & Loops",
        "steps": [
            {
                "title": "List basics",
                "teach": """## Lists — ordered collections

A list stores multiple values in order, in square brackets:

```python
fruits = ["apple", "banana", "cherry"]
```

**Indexing** — access items by position. Positions start at 0:
- `fruits[0]` → "apple" (first)
- `fruits[1]` → "banana" (second)
- `fruits[-1]` → "cherry" (last — negative indexes count from the end)

**Slicing** — get a range of items:
- `fruits[1:]` → ["banana", "cherry"] (from index 1 to end)
- `fruits[:2]` → ["apple", "banana"] (from start to index 2, not including 2)

**Run the code** and predict each result before reading the output.""",
                "code": """fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])     # first
print(fruits[-1])    # last
print(fruits[1:3])   # index 1 and 2 (not 3)
print(fruits[:2])    # first two
print(fruits[2:])    # everything from index 2 onward
print(len(fruits))   # how many items
""",
                "expected": "apple\nelderberry\n['banana', 'cherry']\n['apple', 'banana']\n['cherry', 'date', 'elderberry']\n5",
                "hint": "Indexes start at 0. Negative indexes count from the end: -1 is last, -2 is second to last. Slices go up to but NOT including the end index.",
            },
            {
                "title": "Modifying lists",
                "teach": """## Modifying lists

Lists are mutable — you can change them after creating them.

| Method | What it does |
|--------|-------------|
| `.append(x)` | add x to the end |
| `.insert(i, x)` | insert x at position i |
| `.remove(x)` | remove first occurrence of x |
| `.pop()` | remove and return the last item |
| `.sort()` | sort in place |
| `.reverse()` | reverse in place |

**Run the code** and add a `print(nums)` after each operation to watch the list change step by step.""",
                "code": """nums = [3, 1, 4, 1, 5, 9, 2, 6]
print("start:", nums)

nums.append(7)
print("after append:", nums)

nums.remove(1)        # removes the FIRST 1
print("after remove:", nums)

last = nums.pop()
print("popped:", last)
print("after pop:", nums)

nums.sort()
print("sorted:", nums)
""",
                "expected": "start: [3, 1, 4, 1, 5, 9, 2, 6]\nafter append: [3, 1, 4, 1, 5, 9, 2, 6, 7]\nafter remove: [3, 4, 1, 5, 9, 2, 6, 7]\npopped: 7\nafter pop: [3, 4, 1, 5, 9, 2, 6]\nsorted: [1, 2, 3, 4, 5, 6, 9]",
                "hint": ".remove(x) removes the FIRST occurrence. .pop() removes the last and returns it so you can use the value.",
            },
            {
                "title": "List comprehensions",
                "teach": """## List comprehensions — build lists in one line

Instead of this (4 lines):
```python
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
```

Write this (1 line):
```python
squares = [x ** 2 for x in range(1, 6)]
```

The pattern: `[expression for item in iterable if condition]`

The `if condition` at the end is optional — it filters which items get included.

**Run the code** and experiment — try changing the condition or the expression.""",
                "code": """# Squares of 1-5
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# Only even numbers from 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# All words longer than 4 letters
words = ["hi", "hello", "world", "python", "ok", "code", "learn"]
long_words = [w for w in words if len(w) > 4]
print(long_words)

# Uppercase each word
upper = [w.upper() for w in words]
print(upper)
""",
                "expected": "[1, 4, 9, 16, 25]\n[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n['hello', 'world', 'python', 'learn']\n['HI', 'HELLO', 'WORLD', 'PYTHON', 'OK', 'CODE', 'LEARN']",
                "hint": "Read a comprehension as: 'give me X for each item in Y, but only if Z'. The if part is optional.",
            },
            {
                "title": "zip and enumerate",
                "teach": """## zip and enumerate — powerful loop tools

**`enumerate()`** gives you the index AND the value:
```python
for i, item in enumerate(my_list):
    print(i, item)
```

**`zip()`** loops two lists at the same time, pairing them up:
```python
for a, b in zip(list1, list2):
    print(a, b)
```

These two are used constantly. Memorize them.

**Run the code** and then try using `zip` to create a dict from the two lists using `dict(zip(names, scores))`.""",
                "code": """# enumerate — index + value
animals = ["cat", "dog", "bird", "fish"]
for i, animal in enumerate(animals):
    print(f"{i}: {animal}")

print()

# zip — pair two lists
names = ["Alice", "Bob", "Carol"]
scores = [88, 95, 70]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

print()

# zip to make a dict
score_dict = dict(zip(names, scores))
print(score_dict)
""",
                "expected": "0: cat\n1: dog\n2: bird\n3: fish\n\nAlice scored 88\nBob scored 95\nCarol scored 70\n\n{'Alice': 88, 'Bob': 95, 'Carol': 70}",
                "hint": "enumerate() returns (index, value) pairs. zip() pairs up items by position and stops at the shorter list.",
            },
        ],
    },
    {
        "id": "05_dicts_and_sets",
        "title": "Dicts & Sets",
        "steps": [
            {
                "title": "Dict basics",
                "teach": """## Dicts — key-value storage

A dict (dictionary) maps **keys** to **values**. Like a real dictionary: you look up a word (key) and get its definition (value).

```python
person = {"name": "Jack", "age": 28}
print(person["name"])   # "Jack"
```

**Keys** must be unique and immutable (strings, numbers, tuples).
**Values** can be anything.

If you try to access a key that doesn't exist, Python crashes with a `KeyError`. Use `.get()` to avoid this — it returns `None` (or a default you choose) for missing keys.

**Run the code** and then try accessing a key that doesn't exist two ways: directly (crash) and with .get() (safe).""",
                "code": """person = {
    "name": "Jack",
    "age": 28,
    "city": "New York"
}

print(person["name"])
print(person["age"])
print(len(person))

# Safe access
print(person.get("salary"))         # None — no crash
print(person.get("salary", 0))      # 0 — your default

# Add and update
person["role"] = "founder"
person["age"] = 29
print(person)
""",
                "expected": "Jack\n28\n3\nNone\n0\n{'name': 'Jack', 'age': 29, 'city': 'New York', 'role': 'founder'}",
                "hint": "person[key] crashes if key doesn't exist. person.get(key) returns None. person.get(key, default) returns default.",
            },
            {
                "title": "Looping over dicts",
                "teach": """## Looping over dicts

Three ways to loop:

```python
# Just keys
for key in my_dict:

# Just values
for value in my_dict.values():

# Both (most common)
for key, value in my_dict.items():
```

**Run the code** and see the difference between each approach. The `.items()` version is what you'll use 90% of the time.""",
                "code": """scores = {"Alice": 88, "Bob": 95, "Carol": 70, "Dave": 82}

print("Keys:")
for name in scores:
    print(" ", name)

print("Values:")
for score in scores.values():
    print(" ", score)

print("Both:")
for name, score in scores.items():
    print(f"  {name}: {score}")

# Find the highest scorer
best = max(scores, key=scores.get)
print(f"Best: {best} with {scores[best]}")
""",
                "expected": "Keys:\n  Alice\n  Bob\n  Carol\n  Dave\nValues:\n  88\n  95\n  70\n  82\nBoth:\n  Alice: 88\n  Bob: 95\n  Carol: 70\n  Dave: 82\nBest: Bob with 95",
                "hint": "Use .items() when you need both key and value. max(scores, key=scores.get) finds the key with the highest value.",
            },
            {
                "title": "Dict comprehensions",
                "teach": """## Dict comprehensions

Just like list comprehensions but for dicts:

```python
{key: value for item in iterable}
```

**Run the code** and then try writing a comprehension that creates a dict of only scores above 80.""",
                "code": """words = ["apple", "banana", "kiwi", "fig", "cherry"]

# Word → its length
lengths = {word: len(word) for word in words}
print(lengths)

# Word → uppercase version
upper = {word: word.upper() for word in words}
print(upper)

# Filter: only words longer than 4 letters
long_lengths = {word: len(word) for word in words if len(word) > 4}
print(long_lengths)
""",
                "expected": "{'apple': 5, 'banana': 6, 'kiwi': 4, 'fig': 3, 'cherry': 6}\n{'apple': 'APPLE', 'banana': 'BANANA', 'kiwi': 'KIWI', 'fig': 'FIG', 'cherry': 'CHERRY'}\n{'apple': 5, 'banana': 6, 'cherry': 6}",
                "hint": "Dict comprehension: {key: value for item in iterable if condition}. The if is optional.",
            },
            {
                "title": "Sets",
                "teach": """## Sets — unique values, instant lookup

A set is like a list but:
- **No duplicates** — adding the same item twice has no effect
- **No order** — items have no position
- **Very fast** lookup — checking `if x in my_set` is instant, regardless of size

Sets use `{}` like dicts, but without `key: value` pairs:
```python
my_set = {1, 2, 3}
```

**Main uses:** deduplication, membership testing, set math (overlap, union, difference).

**Run the code** and notice the set operations — these are extremely useful for comparing lists of data.""",
                "code": """# Deduplication
with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(with_dupes))
print(unique)

# Set math
team_a = {"Alice", "Bob", "Carol"}
team_b = {"Bob", "Carol", "Dave"}

print("In both teams:", team_a & team_b)
print("In either team:", team_a | team_b)
print("Only in team A:", team_a - team_b)

# Fast membership check
allowed_users = {"alice", "bob", "carol"}
user = "bob"
if user in allowed_users:
    print(f"{user} is allowed")
""",
                "expected": None,
                "hint": "& is intersection (both), | is union (either), - is difference (in first but not second). Sets automatically remove duplicates.",
            },
        ],
    },
    {
        "id": "06_classes_and_objects",
        "title": "Classes & Objects",
        "steps": [
            {
                "title": "What is a class?",
                "teach": """## Classes — blueprints for objects

A **class** is a blueprint. An **object** (instance) is the actual thing created from that blueprint.

Think of a class like a cookie cutter — the cutter is the class, each cookie you cut is an object.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says: Woof!")
```

- `__init__` runs automatically when you create an instance — it sets up the object
- `self` refers to the specific instance being created/used
- `self.name` stores `name` ON that specific object

**Run the code** and notice: `rex` and `buddy` are separate objects with separate data.""",
                "code": """class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}")

rex = Dog("Rex", "Labrador")
buddy = Dog("Buddy", "Poodle")

rex.bark()
buddy.bark()
rex.describe()

print(rex.name)
print(buddy.breed)
""",
                "expected": "Rex says: Woof!\nBuddy says: Woof!\nRex is a Labrador\nRex\nPoodle",
                "hint": "Each Dog object has its own name and breed. They share the bark() method but their data is separate.",
            },
            {
                "title": "What self really is",
                "teach": """## self is just the instance

`self` sounds mysterious but it's simple: when you call `rex.bark()`, Python translates it to `Dog.bark(rex)` — it passes `rex` as the first argument automatically.

`self` is just the name for "the instance this method was called on." You could technically name it anything (but always call it `self` by convention).

This means:
```python
rex.bark()       # Python calls this
Dog.bark(rex)    # as if you wrote this
```

They're identical.

**Run the code** and see both produce the same output.""",
                "code": """class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

rex = Dog("Rex")

# These two lines do EXACTLY the same thing:
rex.bark()
Dog.bark(rex)

# self IS rex in both cases
print(id(rex))
""",
                "expected": "Rex says: Woof!\nRex says: Woof!",
                "hint": "Python automatically passes the instance as the first argument (self). rex.bark() is just shorthand for Dog.bark(rex).",
            },
            {
                "title": "__repr__ and other magic methods",
                "teach": """## Magic methods — making objects feel native

Python uses `__double_underscore__` methods to make your objects work with built-in syntax:

| Method | What it controls |
|--------|-----------------|
| `__repr__` | what `print(obj)` shows |
| `__add__` | what `obj1 + obj2` does |
| `__eq__` | what `obj1 == obj2` does |
| `__len__` | what `len(obj)` returns |

Without `__repr__`, printing an object shows something ugly like `<__main__.Dog object at 0x10a3b2c>`.

**Always define `__repr__`** — it makes debugging 10x easier.

**Run the code** and see how each magic method makes the object work naturally.""",
                "code": """class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)
print(v1 + v2)
print(v1 == Vector(1, 2))
print(v1 == Vector(9, 9))
print(len(v1))
""",
                "expected": "Vector(1, 2)\nVector(4, 6)\nTrue\nFalse\n2",
                "hint": "__add__ must return a new Vector. __eq__ should compare the x and y values. __repr__ should return a string.",
            },
            {
                "title": "Build a BankAccount",
                "teach": """## Your turn — build a BankAccount class

This is a real challenge. Build it from scratch using what you've learned.

The `BankAccount` class needs:
- `__init__(self, owner, balance=0)` — set up the account
- `deposit(self, amount)` — add to balance, print confirmation
- `withdraw(self, amount)` — subtract from balance, but print an error if there isn't enough money
- `__repr__(self)` — returns something like `BankAccount(Jack, balance=145)`

**Start with the skeleton below and fill in each method.**

This takes real thinking — that's the point. Try it yourself before looking at the hint.""",
                "code": """class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Have {self.balance}, need {amount}")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def __repr__(self):
        return f"BankAccount({self.owner}, balance={self.balance})"


account = BankAccount("Jack", 100)
print(account)
account.deposit(50)
account.withdraw(30)
account.withdraw(500)
print(account)
""",
                "expected": "BankAccount(Jack, balance=100)\nDeposited 50. Balance: 150\nWithdrew 30. Balance: 120\nInsufficient funds. Have 120, need 500\nBankAccount(Jack, balance=120)",
                "hint": "deposit: self.balance += amount. withdraw: check if amount > self.balance first. __repr__: return a formatted string with self.owner and self.balance.",
            },
        ],
    },
    {
        "id": "07_error_handling",
        "title": "Error Handling",
        "steps": [
            {
                "title": "What is an exception?",
                "teach": """## Exceptions — when things go wrong

When something goes wrong, Python creates an **exception object** and raises it. If nothing catches it, your program stops and prints a traceback (the red error text).

**Common exceptions:**
- `ValueError` — right type, wrong value (`int("abc")`)
- `TypeError` — wrong type entirely (`1 + "a"`)
- `KeyError` — dict key doesn't exist
- `IndexError` — list index out of range
- `ZeroDivisionError` — dividing by zero
- `AttributeError` — object doesn't have that attribute

**Run each line one at a time** (comment out the others with `#`) to see each error type. Reading errors is a core skill — you'll see them constantly.""",
                "code": """# Run these one at a time — comment out the others with #

int("abc")

# [1, 2, 3][99]

# {"a": 1}["b"]

# None.upper()

# 1 / 0
""",
                "expected": None,
                "hint": "Comment out all but one line to see each error. Read the LAST line of the error first — it tells you what went wrong.",
            },
            {
                "title": "try / except",
                "teach": """## try / except — catching errors

Instead of crashing, you can catch an exception and handle it:

```python
try:
    result = int("abc")
except ValueError:
    print("That's not a number")
```

- `try:` — run this code
- `except ValueError:` — if a ValueError happens, run this instead

The key: **catch the specific exception you expect**. Don't catch everything — you'll hide real bugs.

**Run the code.** Then change `text = "abc"` to `text = "42"` and run again — the except block is skipped entirely when no error occurs.""",
                "code": """text = "abc"

try:
    number = int(text)
    print(f"Converted successfully: {number}")
except ValueError:
    print(f"Error: '{text}' is not a valid number")

print("Program continues...")
""",
                "expected": "Error: 'abc' is not a valid number\nProgram continues...",
                "hint": "Change text to '42' and re-run. When there's no error, the except block is completely skipped.",
            },
            {
                "title": "else and finally",
                "teach": """## else and finally

```python
try:
    # risky code
except SomeError:
    # handle the error
else:
    # runs ONLY if NO exception occurred
finally:
    # ALWAYS runs — error or not
```

`else` is for code that should only run on success.
`finally` is for cleanup — closing files, connections, etc. It runs no matter what.

**Run the code with both "42" and "abc"** — watch which blocks execute in each case.""",
                "code": """def convert(s):
    print(f"Trying to convert '{s}'...")
    try:
        result = int(s)
    except ValueError:
        print(f"  EXCEPT: '{s}' is not a number")
    else:
        print(f"  ELSE: converted successfully to {result}")
    finally:
        print(f"  FINALLY: always runs")
    print()

convert("42")
convert("hello")
""",
                "expected": "Trying to convert '42'...\n  ELSE: converted successfully to 42\n  FINALLY: always runs\n\nTrying to convert 'hello'...\n  EXCEPT: 'hello' is not a number\n  FINALLY: always runs\n",
                "hint": "else only runs when there's NO exception. finally always runs. Think of finally as guaranteed cleanup.",
            },
            {
                "title": "Custom exceptions",
                "teach": """## Custom exceptions

You can create your own exception types by inheriting from `Exception`. This makes your code clearer — callers know exactly what can go wrong.

```python
class MyError(Exception):
    pass

raise MyError("something went wrong")
```

Custom exceptions can also store extra information beyond just a message:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Need {amount}, have {balance}")
```

**Run the code** and then try changing the amounts so the withdrawal succeeds — the except block won't run.""",
                "code": """class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw {amount}: balance is only {balance}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 250)
    print(f"Success! New balance: {new_balance}")
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"You have {e.balance}, tried to take {e.amount}")
""",
                "expected": "Error: Cannot withdraw 250: balance is only 100\nYou have 100, tried to take 250",
                "hint": "Try withdraw(100, 50) instead — the withdrawal succeeds and the except block is skipped.",
            },
        ],
    },
    {
        "id": "08_modules",
        "title": "Modules",
        "steps": [
            {
                "title": "What is a module?",
                "teach": """## Modules — code you can import

A module is just a `.py` file. Python ships with hundreds of built-in modules — the **standard library** — that you can use for free.

Import a module with `import`:
```python
import math
print(math.pi)
print(math.sqrt(16))
```

Or import specific things from a module:
```python
from math import sqrt, pi
print(sqrt(16))
```

**Run the code** and explore what `math` can do. Then try `import random` and call `random.randint(1, 100)` to get a random number.""",
                "code": """import math

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.floor(3.9))
print(math.ceil(3.1))
print(math.pow(2, 10))

# How many ways can you arrange 5 things?
print(math.factorial(5))
""",
                "expected": "3.141592653589793\n2.718281828459045\n5.0\n3\n4\n1024.0\n120",
                "hint": "math.factorial(5) = 5 × 4 × 3 × 2 × 1 = 120. Try math.log(100) or math.sin(0).",
            },
            {
                "title": "json — saving and loading data",
                "teach": """## json — the universal data format

JSON is how computers share data. It looks like Python dicts and lists. The `json` module converts between Python objects and JSON text.

```python
import json

# Python → JSON text
json.dumps(data)

# JSON text → Python
json.loads(text)
```

Python `None` becomes JSON `null`. Python `True` becomes JSON `true`.

**Run the code** and see the JSON output. Then modify `data` to include a list of skills and re-run.""",
                "code": """import json

data = {
    "name": "Jack",
    "age": 28,
    "skills": ["Python", "FastAPI"],
    "active": True,
    "salary": None
}

# Convert to JSON string
text = json.dumps(data, indent=2)
print(text)

# Convert back to Python
restored = json.loads(text)
print("Round trip ok:", data == restored)
print("Type:", type(restored))
""",
                "expected": None,
                "hint": "json.dumps() converts Python to JSON text. json.loads() converts JSON text back to Python. indent=2 makes it pretty-printed.",
            },
            {
                "title": "datetime — working with time",
                "teach": """## datetime — dates and times

The `datetime` module handles dates, times, and math between them.

```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)
```

`strftime()` formats a datetime as a string:
- `%Y` → 4-digit year
- `%m` → month (01-12)
- `%d` → day (01-31)
- `%A` → full weekday name
- `%B` → full month name

**Run the code** and see the current date and time. Try computing how many days until your next birthday.""",
                "code": """from datetime import datetime, timedelta

now = datetime.now()

print(now)
print(now.strftime("%A, %B %d %Y"))
print(now.strftime("%I:%M %p"))

# Date math
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print("Tomorrow:", tomorrow.date())
print("Last week:", last_week.date())

# Days between two dates
new_years = datetime(2027, 1, 1)
days_left = (new_years - now).days
print(f"Days until 2027: {days_left}")
""",
                "expected": None,
                "hint": "strftime formats a date as a string. timedelta represents a duration. Subtracting two datetimes gives a timedelta.",
            },
            {
                "title": "collections — powerful extras",
                "teach": """## collections — better data structures

The `collections` module has enhanced versions of dicts and lists:

**`Counter`** — counts things automatically:
```python
Counter(["a", "b", "a", "c", "a"])
# Counter({'a': 3, 'b': 1, 'c': 1})
```

**`defaultdict`** — a dict that creates a default for missing keys, so you never get a KeyError:
```python
groups = defaultdict(list)
groups["team_a"].append("Alice")  # no KeyError even if "team_a" didn't exist
```

**Run the code** and then try `Counter` on a string directly (it counts each character).""",
                "code": """from collections import Counter, defaultdict

# Counter — count word frequencies instantly
text = "the cat sat on the mat the cat"
counts = Counter(text.split())
print(counts)
print("Most common:", counts.most_common(2))

print()

# defaultdict — group items without KeyError
grades = [("Alice", 90), ("Bob", 85), ("Alice", 92), ("Bob", 78)]

by_student = defaultdict(list)
for name, grade in grades:
    by_student[name].append(grade)

for name, gs in by_student.items():
    avg = sum(gs) / len(gs)
    print(f"{name}: {gs} — avg {avg:.1f}")
""",
                "expected": None,
                "hint": "Counter(text.split()) counts word frequency. defaultdict(list) creates an empty list automatically for any new key.",
            },
        ],
    },
]
