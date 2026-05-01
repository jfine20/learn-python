print("=" * 50)
print("MODULE 6: Classes & Objects")
print("=" * 50)

import math

# ─────────────────────────────────────────────────
print("\n--- LESSON 1: What `self` actually is ---")
# ─────────────────────────────────────────────────

# A class is a blueprint. An instance is the actual object created from it.
# `self` is just the name for "the instance this method was called on."
# When you call  rex.bark(),  Python translates it to  Dog.bark(rex).

class Dog:
    def __init__(self, name):   # runs automatically when you create an instance
        self.name = name        # store `name` ON the object

    def bark(self):
        print(f"  {self.name} says: Woof!")

rex = Dog("Rex")
buddy = Dog("Buddy")

print("Normal call:")
rex.bark()

print("Explicit call (exactly the same thing):")
Dog.bark(rex)

print("\nEach instance has its own data:")
print(f"  rex.name   = {rex.name}")
print(f"  buddy.name = {buddy.name}")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 2: Instance vs class attributes ---")
# ─────────────────────────────────────────────────

# Instance attribute: unique per object (stored on the instance)
# Class attribute:    shared across ALL instances (stored on the class)

class Counter:
    total = 0           # class attribute

    def __init__(self, name):
        self.name = name        # instance attribute
        Counter.total += 1

a = Counter("a")
b = Counter("b")
c = Counter("c")

print(f"Counter.total = {Counter.total}")   # 3 — shared
print(f"a.name = {a.name}")                 # "a" — unique to a
print(f"a.total = {a.total}")               # 3 — Python looks it up on the class

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 3: Dunder (magic) methods ---")
# ─────────────────────────────────────────────────

# Python uses __dunder__ methods to make objects work with built-in syntax.
# __repr__ → what print() and the REPL show
# __add__  → what + does
# __eq__   → what == does
# __len__  → what len() does

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"v1 = {v1}")                    # uses __repr__
print(f"v1 + v2 = {v1 + v2}")         # uses __add__
print(f"v1 == Vector(1,2): {v1 == Vector(1, 2)}")  # uses __eq__
print(f"len(v1) = {len(v1)}")         # uses __len__

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- LESSON 4: Inheritance ---")
# ─────────────────────────────────────────────────

# A subclass inherits everything from its parent and can override it.
# Use super() to call the parent's version of a method.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

animals = [Dog("Rex"), Cat("Whiskers"), Duck("Donald")]
for animal in animals:
    print(f"  {animal} says: {animal.speak()}")

print("\nThis is polymorphism — same method call, different behavior per type.")

input("\n>>> Press Enter to continue...")

# ─────────────────────────────────────────────────
print("\n--- YOUR TURN ---")
# ─────────────────────────────────────────────────

print("""
Add your code below. Save and run after each one.

1. Build a BankAccount class with:
   - __init__(self, owner, balance=0)
   - deposit(self, amount)
   - withdraw(self, amount) — raise ValueError if not enough funds
   - __repr__ → "BankAccount(Jack, $150.00)"

   Test it:
     account = BankAccount("Jack", 100)
     account.deposit(75)
     account.withdraw(30)
     print(account)        # BankAccount(Jack, $145.00)
     account.withdraw(999) # should raise ValueError

2. Add a __add__ method to BankAccount that merges two accounts:
     a = BankAccount("Jack", 100)
     b = BankAccount("Alice", 200)
     merged = a + b
     print(merged)   # BankAccount(Jack+Alice, $300.00)
""")

# YOUR CODE HERE ↓
