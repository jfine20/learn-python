# Module 0: The Absolute Basics

## What even is code?

Code is just instructions you write for a computer. The computer reads them top to bottom and does exactly what you say — nothing more, nothing less. If you make a typo, it doesn't guess what you meant. It just stops and tells you there's an error.

Python is a **programming language** — a way of writing instructions that both humans can read and computers can understand.

---

## Step 1: Your first line of code

The most important function in Python (at least when learning) is `print()`. It displays something on the screen.

Type this and hit **Run**:

```python
print("Hello, world!")
```

**What you should see:** `Hello, world!`

That's it. You just wrote a program. The `""` quotes tell Python that `Hello, world!` is text (called a **string**). The parentheses `()` are how you "call" (use) a function.

---

## Step 2: Comments

A **comment** is a note you write for yourself (or others) that Python completely ignores. Start a line with `#` to make it a comment.

```python
# This is a comment — Python ignores it
print("But this runs")

print("Hello")  # you can also put comments at the end of a line
```

**Use comments to explain WHY you're doing something, not what.**

---

## Step 3: Math

Python can do math. The operators are:

```python
print(10 + 3)    # addition       → 13
print(10 - 3)    # subtraction    → 7
print(10 * 3)    # multiplication → 30
print(10 / 3)    # division       → 3.333...
print(10 // 3)   # floor division → 3  (drops the decimal)
print(10 % 3)    # modulo (remainder) → 1
print(10 ** 3)   # exponent (power)   → 1000
```

**Run this and check each result.**

The `%` operator (modulo) gives you the **remainder** after dividing. `10 % 3` is 1 because 10 ÷ 3 = 3 with a remainder of 1. This is super useful for checking if a number is even/odd or divisible by something.

```python
print(8 % 2)   # 0 — even numbers have no remainder when divided by 2
print(7 % 2)   # 1 — odd numbers have remainder 1
```

---

## Step 4: Variables

A **variable** stores a value so you can use it later. Use `=` to assign a value to a name.

```python
name = "Jack"
age = 28
height = 5.11

print(name)
print(age)
print(height)
```

**Important:** `=` in Python does NOT mean "equals" like in math. It means **"store this value with this name"**. Read `name = "Jack"` as "name gets Jack."

You can do math with variables:

```python
price = 100
tax_rate = 0.08
tax = price * tax_rate
total = price + tax

print(total)
```

---

## Step 5: Strings

A **string** is text. Wrap it in single or double quotes — both work.

```python
print("Hello")
print('Hello')
print("It's a great day")   # use double quotes if your text has an apostrophe
print('She said "hi"')      # use single quotes if your text has double quotes
```

**String math:**

```python
first = "Jack"
last = "Fine"
full = first + " " + last    # joining strings is called concatenation
print(full)

print("ha" * 3)              # "hahaha" — repeat a string
```

**f-strings** — the cleanest way to mix variables into text:

```python
name = "Jack"
age = 28
print(f"My name is {name} and I am {age} years old.")
```

The `f` before the quote tells Python to look for `{}` and replace what's inside with the variable's value. This is called an **f-string** (formatted string).

---

## Step 6: Indentation — Python's biggest rule

In Python, **indentation matters**. It's how Python knows which code belongs together.

```python
if 5 > 3:
    print("5 is bigger")    # indented — belongs to the if
    print("makes sense")    # also indented — also belongs to the if
print("always runs")        # not indented — runs no matter what
```

Use **4 spaces** for each level of indentation. (In this editor, Tab inserts 4 spaces automatically.)

Get this wrong and Python will give you an `IndentationError`. It's very picky.

---

## Step 7: Reading error messages

Errors are normal. Even experienced programmers see them constantly. When you get one, read it from the **bottom up**:

1. The last line tells you the **type of error** and what went wrong
2. The line above tells you **where** it happened

```python
print("hello"
```

Run that (it's missing the closing `)`) and you'll see a `SyntaxError`. That means Python couldn't even understand what you wrote.

Common errors you'll see:
- **SyntaxError** — you wrote something Python can't parse (typo, missing bracket)
- **NameError** — you used a variable that doesn't exist yet
- **TypeError** — you used the wrong type (e.g., adding a number to a string)
- **IndentationError** — your spacing is wrong

---

## Step 8: Getting input from the user

`input()` pauses the program and waits for you to type something:

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

**Important:** `input()` always returns a **string**, even if you type a number. To use it as a number, convert it:

```python
age_text = input("How old are you? ")
age = int(age_text)    # convert string "28" to integer 28
print(f"In 10 years you'll be {age + 10}")
```

---

## Now put it all together

Build a tiny program that:
1. Asks for the user's name
2. Asks for their birth year (as a number)
3. Calculates their age (2026 minus birth year)
4. Prints a message like: `"Hi Jack! You are 28 years old."`

```python
name = input("What's your name? ")
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year
print(f"Hi {name}! You are {age} years old.")
```

**Try running it.** Type your name and birth year when prompted.
