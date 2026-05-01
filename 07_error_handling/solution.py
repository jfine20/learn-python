# Module 07 — Solutions

# ── Exercise 1 ────────────────────────────────────────────────────────────────
exceptions = [
    ("int('abc')",        lambda: int("abc")),          # ValueError
    ("[1,2,3][10]",       lambda: [1, 2, 3][10]),       # IndexError
    ("dict['missing']",   lambda: {"k": "v"}["missing"]), # KeyError
    ("None.upper()",      lambda: None.upper()),         # AttributeError
    ("1 / 0",             lambda: 1 / 0),                # ZeroDivisionError
]
for label, fn in exceptions:
    try:
        fn()
    except Exception as e:
        print(f"{label:25} → {type(e).__name__}: {e}")

# ── Exercise 2 ────────────────────────────────────────────────────────────────
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # message + None

# ── Exercise 3 ────────────────────────────────────────────────────────────────
def read_number(s):
    try:
        result = int(s)
    except ValueError:
        print(f"Not a number: {s}")
    else:
        print(f"Converted: {result}")
    finally:
        print(f"Attempted conversion of: {s}")

read_number("42")
read_number("hello")

# ── Exercise 4 ────────────────────────────────────────────────────────────────
def lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return f"KeyError: '{key}' not found"
    except TypeError:
        return f"TypeError: can't index {type(data).__name__}"

print(lookup({"a": 1}, "a"))
print(lookup({"a": 1}, "b"))
print(lookup(None, "a"))

# ── Exercise 5 ────────────────────────────────────────────────────────────────
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}: balance is only {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)

# ── Exercise 6 ────────────────────────────────────────────────────────────────
def logged_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: division by zero")
        raise   # re-raises the current exception without losing the traceback

try:
    logged_divide(1, 0)
except ZeroDivisionError:
    print("Caught in outer scope")
