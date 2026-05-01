# Module 06 — Classes & Objects
# Run: python 06_classes_and_objects/exercise.py

# ── Exercise 1 ────────────────────────────────────────────────────────────────
# self is just the instance. Prove it.
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

rex = Dog("Rex")
# TODO: call bark() two ways:
#   1. The normal way: rex.bark()
#   2. The explicit way: Dog.bark(rex)
# They should print the same thing.


# ── Exercise 2 ────────────────────────────────────────────────────────────────
# Build a BankAccount class.
# TODO: create a BankAccount class with:
#   - __init__(self, owner, balance=0)
#   - deposit(self, amount) — adds to balance
#   - withdraw(self, amount) — subtracts, but raises ValueError if insufficient funds
#   - __repr__(self) — returns "BankAccount(owner=Jack, balance=100)"

class BankAccount:
    pass  # TODO


# ── Exercise 3 ────────────────────────────────────────────────────────────────
# Class attribute vs instance attribute.
class Counter:
    total = 0   # shared across all instances

    def __init__(self, name):
        self.name = name
        Counter.total += 1  # increment class-level count

# TODO: create 3 Counter instances. Print Counter.total after each.
# Then print the `total` attribute from one instance — what do you get?


# ── Exercise 4 ────────────────────────────────────────────────────────────────
# Dunder methods — make a Vector class that supports math operators.
# TODO: create a Vector class with:
#   - __init__(x, y)
#   - __repr__: "Vector(1, 2)"
#   - __add__: Vector(1,2) + Vector(3,4) = Vector(4,6)
#   - __eq__: Vector(1,2) == Vector(1,2) → True
#   - __len__: always returns 2 (it's 2D)

class Vector:
    pass  # TODO


# ── Exercise 5 ────────────────────────────────────────────────────────────────
# Inheritance.
# TODO: create a base class `Shape` with a method `area()` that raises
# NotImplementedError. Then create `Rectangle` and `Circle` subclasses
# that implement area() correctly.
# Create one of each and print their areas.

import math

class Shape:
    pass  # TODO
