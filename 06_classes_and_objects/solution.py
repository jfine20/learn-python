# Module 06 — Solutions
import math

# ── Exercise 1 ────────────────────────────────────────────────────────────────
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

rex = Dog("Rex")
rex.bark()          # normal call — Python passes rex as self
Dog.bark(rex)       # explicit — identical result

# ── Exercise 2 ────────────────────────────────────────────────────────────────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: have {self.balance}, need {amount}")
        self.balance -= amount

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

account = BankAccount("Jack", 100)
account.deposit(50)
print(account)          # BankAccount(owner=Jack, balance=150)
account.withdraw(30)
print(account)          # BankAccount(owner=Jack, balance=120)
try:
    account.withdraw(500)
except ValueError as e:
    print(e)

# ── Exercise 3 ────────────────────────────────────────────────────────────────
class Counter:
    total = 0
    def __init__(self, name):
        self.name = name
        Counter.total += 1

a = Counter("a"); print(Counter.total)  # 1
b = Counter("b"); print(Counter.total)  # 2
c = Counter("c"); print(Counter.total)  # 3
print(a.total)   # 3 — Python looks up `total` on the class since it's not on the instance

# ── Exercise 4 ────────────────────────────────────────────────────────────────
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
print(v1 + v2)          # Vector(4, 6)
print(v1 == Vector(1, 2))  # True
print(len(v1))           # 2

# ── Exercise 5 ────────────────────────────────────────────────────────────────
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area():.2f}")
