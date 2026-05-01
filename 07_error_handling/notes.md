# Module 7: Error Handling

## What is an exception?

When something goes wrong, Python creates an **exception object** and "raises" it. If nothing catches it, the program stops and prints a traceback (the error message you see in red).

Error handling is how you catch those exceptions and decide what to do instead of crashing.

---

## Step 1: See some common errors

Run each of these one at a time to see what error it produces:

```python
int("abc")         # ValueError: invalid literal for int()
```

```python
[1, 2, 3][10]      # IndexError: list index out of range
```

```python
{"key": "val"}["missing"]   # KeyError: 'missing'
```

```python
None.upper()       # AttributeError: 'NoneType' object has no attribute 'upper'
```

```python
1 / 0              # ZeroDivisionError: division by zero
```

---

## Step 2: Catching exceptions with try / except

Instead of crashing, catch the error and handle it:

```python
text = "abc"

try:
    number = int(text)
    print(f"Converted: {number}")
except ValueError:
    print(f"'{text}' is not a valid number")
```

**Try changing `text` to `"42"` and run again** — when it works, the `except` block is skipped entirely.

---

## Step 3: else and finally

```python
def convert(s):
    try:
        result = int(s)
    except ValueError:
        print(f"Could not convert '{s}'")
    else:
        print(f"Success! Got {result}")    # runs ONLY if no exception
    finally:
        print(f"Done with '{s}'")          # ALWAYS runs, no matter what

convert("42")
print()
convert("hello")
```

**What you should see:** The `else` block only runs on success. The `finally` block runs both times.

Use `finally` for cleanup — closing files, database connections, etc.

---

## Step 4: Catching specific vs broad exceptions

Always catch the **most specific** exception you can. If you catch everything, you'll hide bugs.

```python
def safe_lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return f"Key '{key}' not found"
    except TypeError:
        return f"Can't index a {type(data).__name__}"

print(safe_lookup({"a": 1}, "a"))       # 1
print(safe_lookup({"a": 1}, "b"))       # Key 'b' not found
print(safe_lookup(None, "a"))           # Can't index a NoneType
```

---

## Step 5: Custom exceptions

You can create your own exception types. This lets callers catch your specific error without catching everything.

```python
class InsufficientFundsError(Exception):
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
    result = withdraw(100, 250)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"You have {e.balance}, tried to take {e.amount}")
```

**Try changing the amounts** so the withdrawal succeeds — notice the except block is skipped.

---

## Step 6: Re-raising

Sometimes you want to log an error but still let it crash (or be caught by code higher up):

```python
def process(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print(f"[LOG] Bad input: {data!r}")
        raise    # re-raises the same exception

try:
    process("bad")
except ValueError as e:
    print(f"Caught in outer code: {e}")
```

`raise` with no argument re-raises the current exception without losing the traceback.

---

## Step 7: When NOT to use exceptions

Don't use exceptions for things you expect to happen — use `if`:

```python
# BAD — using exceptions as if/else
try:
    value = my_dict["key"]
except KeyError:
    value = "default"

# GOOD — this is what .get() is for
value = my_dict.get("key", "default")
```

Exceptions are for **unexpected** failures. If you're expecting a condition, check for it with `if`.

---

## Now try it yourself

Write a function `parse_age(s)` that:
1. Converts `s` to an integer — if it fails, raise `ValueError` with message "Not a number"
2. If the number is negative, raise `ValueError` with message "Age can't be negative"
3. If the number is over 150, raise `ValueError` with message "That's not a real age"
4. Otherwise return the number

```python
print(parse_age("25"))     # 25
print(parse_age("abc"))    # ValueError: Not a number
print(parse_age("-5"))     # ValueError: Age can't be negative
print(parse_age("200"))    # ValueError: That's not a real age
```
