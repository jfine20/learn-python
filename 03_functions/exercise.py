# Module 03 — Functions
# Run: python 03_functions/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Functions are objects. Prove it.
def double(x):
    return x * 2

# TODO: assign `double` to a new variable `times_two` and call it with 5.
# Then print the type of `double` — what is it?


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# Functions can be passed as arguments.
def apply(func, value):
    return func(value)

# TODO: call `apply` with `double` and the number 7.
# Then write a `triple` function and call apply with that too.


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# The mutable default argument gotcha.
def append_to(item, the_list=[]):
    the_list.append(item)
    return the_list

# TODO: call append_to("a"), then append_to("b"), then append_to("c").
# Print the result each time. What do you notice? Why does this happen?


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# Fix the function above so each call starts with a fresh list.
def append_to_fixed(item, the_list=None):
    pass  # TODO: implement the fix


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# *args — a function that takes any number of numbers and returns their sum.
# TODO: write `my_sum(*args)` without using the built-in sum().


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# **kwargs — a function that builds a profile string from keyword arguments.
# Example: profile(name="Jack", role="founder") → "name=Jack, role=founder"
# TODO: write `profile(**kwargs)`.


# ── Exercise 7 ────────────────────────────────────────────────────────────────
# Closures — a function that remembers its enclosing scope.
# TODO: write a function `make_multiplier(n)` that RETURNS a function.
# The returned function should multiply its argument by n.
#
# Example:
#   triple = make_multiplier(3)
#   print(triple(10))  # 30
#   print(triple(7))   # 21

def make_multiplier(n):
    pass  # TODO
