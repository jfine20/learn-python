print("=" * 50)
print("MODULE 2: Control Flow")
print("=" * 50)

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: Truthiness ---")
# ─────────────────────────────────────────────────

# Python doesn't need == True. Every object has a truth value.
# FALSY: None, 0, 0.0, "", [], {}, set(), ()
# TRUTHY: everything else

print("These are all FALSY (treated as False in if/while):")
falsy_values = [None, 0, 0.0, "", [], {}, set()]
for v in falsy_values:
    if not v:
        print(f"  {v!r:10} → falsy")

print("\nThese are TRUTHY (even though they might look 'empty' or 'zero-ish'):")
truthy_values = [1, -1, "0", " ", [0], {"key": None}]
for v in truthy_values:
    if v:
        print(f"  {v!r:15} → truthy")

print('\nSo instead of:  if len(my_list) > 0:')
print('Python style is: if my_list:')

my_list = []
if my_list:
    print("has items")
else:
    print("list is empty")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: and / or return VALUES, not True/False ---")
# ─────────────────────────────────────────────────

# `or`  returns the FIRST truthy value, or the last value if all are falsy
# `and` returns the FIRST falsy value, or the last value if all are truthy

print("or examples:")
print(f"  None or 'fallback'     = {None or 'fallback'}")
print(f"  'real' or 'fallback'   = {'real' or 'fallback'}")
print(f"  0 or '' or 'last'      = {0 or '' or 'last'}")

print("\nand examples:")
print(f"  0 and 'never reached'  = {0 and 'never reached'}")
print(f"  1 and 'reached'        = {1 and 'reached'}")
print(f"  'a' and 'b' and 'c'    = {'a' and 'b' and 'c'}")

print("\nReal use — safe default value:")
username = None
display = username or "Anonymous"
print(f"  username = None  →  display = '{display}'")

print("\nReal use — safe attribute access (won't crash if user is None):")
user = None
name = user and user.get("name")
print(f"  user = None  →  name = {name}")

user = {"name": "Jack"}
name = user and user.get("name")
print(f"  user = dict  →  name = {name}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: for loops work on ANYTHING iterable ---")
# ─────────────────────────────────────────────────

# Python's for loop doesn't use indexes. It asks: "give me the next item."
# Anything that can give you items one at a time is iterable.

print("Looping over a list:")
for item in [10, 20, 30]:
    print(f"  {item}")

print("\nLooping over a string (each character):")
for char in "Python":
    print(f"  '{char}'")

print("\nLooping over a dict (gives you keys):")
for key in {"name": "Jack", "age": 28}:
    print(f"  key: {key}")

print("\nenumerate() gives you index + value:")
for i, char in enumerate("abc"):
    print(f"  index {i} → '{char}'")

print("\nzip() pairs up two lists:")
names  = ["Alice", "Bob", "Carol"]
scores = [95, 80, 88]
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: range() is lazy ---")
# ─────────────────────────────────────────────────

# range(1000000) does NOT create a list of a million numbers.
# It creates an object that generates numbers ONE AT A TIME, on demand.

r = range(10)
print(f"type(range(10)) = {type(r)}")   # <class 'range'>
print(f"range(10)[4]    = {r[4]}")      # can index directly — no list needed
print(f"list(range(5))  = {list(range(5))}")  # convert to list if you need all values

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 5: break and continue ---")
# ─────────────────────────────────────────────────

print("continue skips the rest of this iteration:")
for n in range(6):
    if n == 3:
        continue    # jump back to top of loop
    print(f"  {n}")

print("\nbreak exits the loop entirely:")
for n in range(10):
    if n == 4:
        break
    print(f"  {n}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Try these. Edit this file, add your code at the bottom, save, and run.

1. FizzBuzz — print numbers 1 to 20.
   For multiples of 3 print "Fizz".
   For multiples of 5 print "Buzz".
   For multiples of both print "FizzBuzz".
   Hint: use the % (modulo) operator — 9 % 3 == 0 means 9 is divisible by 3.

2. Loop over this list and print only the words longer than 4 characters:
   words = ["hi", "hello", "world", "python", "ok", "code"]

3. Use zip() to print "Alice scored 95", "Bob scored 80", etc:
   names  = ["Alice", "Bob", "Carol"]
   scores = [95, 80, 88]

Add your code below this print statement, save the file, and run it.
""")

# YOUR CODE HERE ↓
