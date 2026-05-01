# Module 02 — Solutions

# ── Exercise 1 ────────────────────────────────────────────────────────────────
values = [0, 1, "", "0", [], [0], None, {}, {"key": None}]
for v in values:
    label = "truthy" if v else "falsy"
    print(f"{v!r:20} is {label}")
# Notable: "0" is truthy (non-empty string), [0] is truthy (non-empty list),
# {"key": None} is truthy (non-empty dict even though the value is None)

# ── Exercise 2 ────────────────────────────────────────────────────────────────
print(None or "fallback")        # "fallback" — None is falsy, so `or` keeps going
print("real" or "fallback")      # "real" — truthy, `or` stops immediately
print(0 and "never reached")     # 0 — falsy, `and` stops immediately
print(1 and "reached")           # "reached" — 1 is truthy, `and` returns the right side
print([] or {} or "last resort") # "last resort" — first two are falsy

# ── Exercise 3 ────────────────────────────────────────────────────────────────
user = None
admin = bool(user and user.get("admin"))
print(admin)  # False — user is None, short-circuit prevents user.get() from running

user = {"admin": True}
admin = bool(user and user.get("admin"))
print(admin)  # True

# ── Exercise 4 ────────────────────────────────────────────────────────────────
for i, char in enumerate("Python"):
    print(f"index {i}: {char}")
# enumerate() wraps an iterable and yields (index, value) tuples.

# ── Exercise 5 ────────────────────────────────────────────────────────────────
r = range(10)
print(type(r))   # <class 'range'>
print(r[4])      # 4 — range supports indexing without materializing the list

# ── Exercise 6 ────────────────────────────────────────────────────────────────
for n in range(1, 31):
    output = ""
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    print(output or n)
# `output or n` — if output is empty string (falsy), print n instead.
# This avoids a separate else branch.

# ── Exercise 7 ────────────────────────────────────────────────────────────────
for n in range(20):
    if n % 2 == 0:
        continue      # skip back to top of loop
    if n > 13:
        break         # exit loop entirely
    print(n)
# Prints: 1, 3, 5, 7, 9, 11, 13
