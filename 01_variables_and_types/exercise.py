print("=" * 50)
print("MODULE 1: Variables & Types")
print("=" * 50)

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: A variable is a name tag, not a box ---")
# ─────────────────────────────────────────────────

# In most languages, a variable is like a box: you put a value IN it.
# In Python, a variable is a name tag that POINTS TO an object.
# The object lives in memory. The name just references it.

x = 5
y = x       # y is now ANOTHER name tag pointing to the same 5
x = 10      # x now points to 10. The original 5 object is untouched.

print(f"x = {x}")   # 10
print(f"y = {y}")   # still 5 — y was never tied to x, it pointed to the object

print("\nThis matters a lot with lists (which are mutable):")
a = [1, 2, 3]
b = a           # b points to the SAME list object as a
a.append(99)

print(f"a = {a}")   # [1, 2, 3, 99]
print(f"b = {b}")   # [1, 2, 3, 99] — same object! b "saw" the change

print("\nProof — id() shows the memory address of an object:")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"Same object? {id(a) == id(b)}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: Mutable vs Immutable ---")
# ─────────────────────────────────────────────────

# Immutable = can NEVER be changed after creation: int, str, float, tuple, bool
# Mutable   = CAN be changed in place:             list, dict, set

print("Strings are immutable. Watch:")
s = "hello"
print(f"Before: s = '{s}', id = {id(s)}")
s = s + " world"   # This does NOT change the string. It creates a NEW one.
print(f"After:  s = '{s}', id = {id(s)}")
print("The id changed — it's a completely different object in memory.")

print("\nLists are mutable. Watch:")
lst = [1, 2, 3]
print(f"Before: lst = {lst}, id = {id(lst)}")
lst.append(4)
print(f"After:  lst = {lst}, id = {id(lst)}")
print("The id stayed the same — the SAME object was modified.")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: Types live on objects, not variables ---")
# ─────────────────────────────────────────────────

# The name tag has no type. The object it points to does.
thing = 42
print(f"thing = {thing}, type = {type(thing)}")

thing = "now it's a string"
print(f"thing = {thing}, type = {type(thing)}")

thing = [1, 2, 3]
print(f"thing = {thing}, type = {type(thing)}")

print("\nCheck types with type() or isinstance():")
print(f"isinstance(42, int)   = {isinstance(42, int)}")
print(f"isinstance(42, str)   = {isinstance(42, str)}")
print(f"isinstance(42, (int, float)) = {isinstance(42, (int, float))}")  # check multiple

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: None ---")
# ─────────────────────────────────────────────────

# None means "no value". There is only ONE None object in all of Python.
x = None
y = None
print(f"x is y: {x is y}")   # True — they literally point to the same object

# Always use `is` to check for None, not ==
# `is` checks identity (same object), `==` checks equality (same value)
if x is None:
    print("x is None")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Try these one at a time. Edit this file, uncomment a line, save, and run.

1. Make two lists that are INDEPENDENT copies (changing one doesn't affect the other).
   Hint: try  b = a.copy()  instead of  b = a

2. Uncomment this and predict what happens before running:
   # s = "hello"
   # try:
   #     s[0] = "H"
   # except TypeError as e:
   #     print(f"Error: {e}")

3. Uncomment this and explain the result in a comment:
   # x = 5
   # y = 5
   # print(id(x) == id(y))   # True or False?
   #
   # x = 1000
   # y = 1000
   # print(id(x) == id(y))   # True or False? Why different?

Edit the file, uncomment the blocks above, save, and run again.
""")
