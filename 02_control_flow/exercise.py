# Module 02 — Control Flow
# Run: python 02_control_flow/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# Predict: truthy or falsy? Then verify with bool()
values = [0, 1, "", "0", [], [0], None, {}, {"key": None}]
# TODO: loop through values and print: "<value> is truthy/falsy"


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# `and` and `or` return VALUES, not True/False.
# TODO: without running it, predict what each prints. Then run.
print(None or "fallback")
print("real" or "fallback")
print(0 and "never reached")
print(1 and "reached")
print([] or {} or "last resort")


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# Safe dictionary access using `and` short-circuit.
user = None
# TODO: write ONE line that sets admin = True if user is a dict with key "admin",
# otherwise admin = False. It must not crash when user is None.


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# for loops work on any iterable, not just lists.
# TODO: iterate over the string "Python" and print each character with its index.
# Use enumerate() — look up how it works if you don't know.


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# range() is lazy — it doesn't store all the numbers.
# TODO: prove it. Print type(range(10)). Then print the 5th element without
# converting to a list.


# ── Exercise 6 ────────────────────────────────────────────────────────────────
# FizzBuzz — classic, but focus on the logic structure.
# Print numbers 1-30. For multiples of 3 print "Fizz", multiples of 5 print "Buzz",
# multiples of both print "FizzBuzz".
# TODO: write it. Then rewrite it using a single print() call per iteration
# (hint: build the output string first, then print).


# ── Exercise 7 ────────────────────────────────────────────────────────────────
# Loop control: break and continue
# TODO: loop through range(20). Skip even numbers (continue). Stop entirely
# when you hit a number > 13 (break). Print each number you don't skip.
