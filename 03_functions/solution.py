# Module 03 — Solutions

# ── Exercise 1 ────────────────────────────────────────────────────────────────
def double(x):
    return x * 2

times_two = double
print(times_two(5))      # 10
print(type(double))      # <class 'function'>

# ── Exercise 2 ────────────────────────────────────────────────────────────────
def apply(func, value):
    return func(value)

print(apply(double, 7))  # 14

def triple(x):
    return x * 3

print(apply(triple, 7))  # 21

# ── Exercise 3 ────────────────────────────────────────────────────────────────
def append_to(item, the_list=[]):
    the_list.append(item)
    return the_list

print(append_to("a"))  # ["a"]
print(append_to("b"))  # ["a", "b"]  ← surprise!
print(append_to("c"))  # ["a", "b", "c"]
# The [] default is created ONCE when Python reads the def statement.
# Every call that doesn't pass `the_list` gets the SAME list object.

# ── Exercise 4 ────────────────────────────────────────────────────────────────
def append_to_fixed(item, the_list=None):
    if the_list is None:
        the_list = []       # new list created each call
    the_list.append(item)
    return the_list

print(append_to_fixed("a"))  # ["a"]
print(append_to_fixed("b"))  # ["b"]  — fresh list

# ── Exercise 5 ────────────────────────────────────────────────────────────────
def my_sum(*args):
    total = 0
    for n in args:
        total += n
    return total

print(my_sum(1, 2, 3, 4))   # 10
print(my_sum(10, 20))       # 30

# ── Exercise 6 ────────────────────────────────────────────────────────────────
def profile(**kwargs):
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())

print(profile(name="Jack", role="founder"))  # name=Jack, role=founder

# ── Exercise 7 ────────────────────────────────────────────────────────────────
def make_multiplier(n):
    def multiplier(x):
        return x * n     # `n` is captured from the enclosing scope — this is a closure
    return multiplier

triple = make_multiplier(3)
print(triple(10))   # 30
print(triple(7))    # 21

# The `n` value is "closed over" — it lives in the function's __closure__,
# not in any local or global scope. Each call to make_multiplier creates
# a brand new closure with its own `n`.
print(triple.__closure__[0].cell_contents)  # 3
