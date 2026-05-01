print("=" * 50)
print("MODULE 7: Error Handling")
print("=" * 50)

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: Exceptions are objects ---")
# ─────────────────────────────────────────────────

# An exception is just a Python object.
# When something goes wrong, Python creates one and "raises" it.
# The call stack unwinds looking for a matching `except` block.
# If nothing catches it, the program crashes and prints the traceback.

print("Common exception types:")
errors = [
    ("int('abc')",        lambda: int("abc")),
    ("[1,2,3][99]",       lambda: [1,2,3][99]),
    ("{}['missing']",     lambda: {}["missing"]),
    ("None.upper()",      lambda: None.upper()),
    ("1 / 0",             lambda: 1 / 0),
]
for label, fn in errors:
    try:
        fn()
    except Exception as e:
        print(f"  {label:20} → {type(e).__name__}: {e}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: try / except / else / finally ---")
# ─────────────────────────────────────────────────

# try:     — run this code
# except:  — if an exception is raised, handle it here
# else:    — runs ONLY if NO exception was raised
# finally: — ALWAYS runs, no matter what (cleanup goes here)

def convert(s):
    try:
        result = int(s)
    except ValueError:
        print(f"  '{s}' is not a valid integer")
    else:
        print(f"  Converted '{s}' → {result}")
    finally:
        print(f"  (finished attempt for '{s}')")

convert("42")
print()
convert("hello")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: Catch specific, not broad ---")
# ─────────────────────────────────────────────────

# Never do `except Exception:` for everything — you'll hide real bugs.
# Catch the specific exception you expect and know how to handle.

def safe_get(data, key):
    try:
        return data[key]
    except KeyError:
        return f"(key '{key}' not found)"
    except TypeError:
        return f"(can't index {type(data).__name__})"

print(f"  safe_get({{'a': 1}}, 'a')    = {safe_get({'a': 1}, 'a')}")
print(f"  safe_get({{'a': 1}}, 'b')    = {safe_get({'a': 1}, 'b')}")
print(f"  safe_get(None, 'a')          = {safe_get(None, 'a')}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: Custom exceptions ---")
# ─────────────────────────────────────────────────

# You can create your own exception types by inheriting from Exception.
# This lets callers catch your specific error without catching everything.

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount}: balance is only ${balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

print("Custom exception demo:")
try:
    new_balance = withdraw(100, 250)
except InsufficientFundsError as e:
    print(f"  Caught: {e}")
    print(f"  Balance was: {e.balance}, tried to withdraw: {e.amount}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 5: Re-raising ---")
# ─────────────────────────────────────────────────

# Sometimes you want to log an error but still let it propagate upward.
# `raise` with no argument re-raises the current exception.

def logged_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("  [LOG] ZeroDivisionError caught in logged_divide")
        raise   # re-raise — caller still gets the exception

print("Re-raise demo:")
try:
    logged_divide(10, 0)
except ZeroDivisionError:
    print("  Caught again in outer scope")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Add your code below. Save and run after each one.

1. Write a function `parse_age(s)` that:
   - Converts s to an integer
   - Raises ValueError if s is not a number
   - Raises ValueError if the number is negative
   - Returns the age if valid
   Test with: "25", "abc", "-5"

2. Create a custom exception `ValidationError` and write a function
   `validate_email(email)` that raises it if the email doesn't contain "@".
   Test it with "jack@example.com" and "notanemail".

3. Write `safe_open(filepath)` that tries to open and read a file.
   If the file doesn't exist (FileNotFoundError), return an empty string.
   Use a finally block to print "Attempted to read <filepath>" every time.
""")

# YOUR CODE HERE ↓
