# Module 07 — Error Handling
# Run: python 07_error_handling/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Identify the exception type before running.
# TODO: predict which exception each line raises. Then verify by running them
# one at a time (comment the others out).

# int("abc")
# [1, 2, 3][10]
# {"key": "val"}["missing"]
# None.upper()
# 1 / 0


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# Catch specific exceptions.
def safe_divide(a, b):
    # TODO: return a / b, but handle the case where b is 0.
    # Return None and print a message instead of crashing.
    pass


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# else and finally.
def read_number(s):
    # TODO: try to convert s to int.
    # If it works (else), print "Converted: <value>".
    # If it fails, print "Not a number: <s>".
    # In finally, always print "Attempted conversion of: <s>".
    pass

read_number("42")
read_number("hello")


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# Catch multiple exception types.
def lookup(data, key):
    # TODO: handle both KeyError (key doesn't exist) and
    # TypeError (data isn't subscriptable — e.g., None["key"]).
    # Return the value or an error message string.
    pass

print(lookup({"a": 1}, "a"))       # 1
print(lookup({"a": 1}, "b"))       # key error
print(lookup(None, "a"))           # type error


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# Custom exceptions.
# TODO: create a custom exception `InsufficientFundsError` that takes
# `balance` and `amount` as arguments and formats a message like:
# "Cannot withdraw 150: balance is only 100"
#
# Then raise it from a withdraw() function.

class InsufficientFundsError(Exception):
    pass  # TODO

def withdraw(balance, amount):
    pass  # TODO


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# Re-raising exceptions.
# Sometimes you want to log an error but still let it propagate up.
# TODO: write a function `logged_divide(a, b)` that catches ZeroDivisionError,
# prints "ERROR: division by zero", then re-raises the original exception.

def logged_divide(a, b):
    pass  # TODO
