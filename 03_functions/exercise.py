print("=" * 50)
print("MODULE 3: Functions")
print("=" * 50)

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: Functions are objects ---")
# ─────────────────────────────────────────────────

# A function is just an object — like a list or a string.
# You can store it in a variable, pass it to another function, put it in a list.

def double(x):
    return x * 2

print(f"type(double) = {type(double)}")   # <class 'function'>

# Assign to a new variable — same function, different name tag
times_two = double
print(f"times_two(5) = {times_two(5)}")  # 10

# Pass a function as an argument
def apply(func, value):
    return func(value)

print(f"apply(double, 7) = {apply(double, 7)}")   # 14

# This is what makes things like sorted(key=...) work
words = ["banana", "fig", "apple"]
print(f"sorted by length: {sorted(words, key=len)}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: Scope — where Python looks for names (LEGB) ---")
# ─────────────────────────────────────────────────

# When Python sees a name, it searches in this order:
# L = Local (inside current function)
# E = Enclosing (outer functions)
# G = Global (module level)
# B = Built-in (len, print, etc.)

x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(f"  inner sees x = '{x}'")   # finds 'enclosing' — E before G
    inner()

print("Scope demo:")
outer()
print(f"Global x is still: '{x}'")   # unchanged

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: The mutable default argument trap ---")
# ─────────────────────────────────────────────────

# Default values are evaluated ONCE when the function is DEFINED.
# Not each time the function is called. This surprises everyone.

def broken_append(item, the_list=[]):   # this [] is created exactly once
    the_list.append(item)
    return the_list

print("Calling broken_append three times:")
print(f"  call 1: {broken_append('a')}")   # ['a']
print(f"  call 2: {broken_append('b')}")   # ['a', 'b']  ← surprise!
print(f"  call 3: {broken_append('c')}")   # ['a', 'b', 'c']

print("\nThe fix — use None as the default:")

def fixed_append(item, the_list=None):
    if the_list is None:
        the_list = []       # new list created each call
    the_list.append(item)
    return the_list

print(f"  call 1: {fixed_append('a')}")   # ['a']
print(f"  call 2: {fixed_append('b')}")   # ['b']  ← correct

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: *args and **kwargs ---")
# ─────────────────────────────────────────────────

# *args  = any number of positional arguments → collected into a tuple
# **kwargs = any number of keyword arguments  → collected into a dict

def show_args(*args, **kwargs):
    print(f"  args   = {args}")
    print(f"  kwargs = {kwargs}")

print("Calling show_args(1, 2, 3, color='red', size='large'):")
show_args(1, 2, 3, color="red", size="large")

print("\nReal use — a function that accepts any number of numbers:")

def my_sum(*args):
    total = 0
    for n in args:
        total += n
    return total

print(f"  my_sum(1, 2, 3)     = {my_sum(1, 2, 3)}")
print(f"  my_sum(10, 20)      = {my_sum(10, 20)}")
print(f"  my_sum(1,2,3,4,5,6) = {my_sum(1,2,3,4,5,6)}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 5: Closures ---")
# ─────────────────────────────────────────────────

# A closure is a function that remembers the variables from where it was created,
# even after that outer function has finished running.

def make_multiplier(n):
    def multiplier(x):
        return x * n    # `n` is captured from the enclosing scope
    return multiplier   # return the function itself, not the result

triple = make_multiplier(3)
double_fn = make_multiplier(2)

print(f"triple(10) = {triple(10)}")     # 30
print(f"triple(7)  = {triple(7)}")      # 21
print(f"double_fn(5) = {double_fn(5)}") # 10

print(f"\nThe captured `n` lives in: {triple.__closure__[0].cell_contents}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Add your code below. Save and run after each one.

1. Write a function `profile(**kwargs)` that takes any keyword arguments
   and returns them as a string like: "name=Jack, role=founder"
   Test it: print(profile(name="Jack", role="founder", age=28))

2. Write `make_adder(n)` — returns a function that adds n to its argument.
   Example:
     add5 = make_adder(5)
     print(add5(10))   # 15
     print(add5(3))    # 8

3. Write `apply_twice(func, value)` — applies func to value, then to the result.
   Example:
     apply_twice(double, 3)   # double(double(3)) = 12
""")

# YOUR CODE HERE ↓
