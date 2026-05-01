# Module 6: Classes & Objects

## What is a class?

A class is a **blueprint** for creating objects. An object bundles together **data** (attributes) and **behavior** (methods) into one thing.

Think of a class like a cookie cutter — the cutter is the class, each cookie is an object (instance).

---

## Step 1: Your first class

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

rex = Dog("Rex", "Labrador")
buddy = Dog("Buddy", "Poodle")

rex.bark()
buddy.bark()
print(rex.name)
print(buddy.breed)
```

**What you should see:**
```
Rex says: Woof!
Buddy says: Woof!
Rex
Poodle
```

---

## Step 2: What `self` actually is

`self` is just the name for "the instance this method was called on." When you write `rex.bark()`, Python translates it to `Dog.bark(rex)` — passing `rex` as the first argument automatically.

Prove it:

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says: Woof!")

rex = Dog("Rex")
rex.bark()           # normal way
Dog.bark(rex)        # exact same thing
```

**What you should see:** Same output twice. They are identical calls.

---

## Step 3: `__init__` sets up the object

`__init__` runs automatically when you create an instance. Use it to set up the initial state.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance is only {self.balance}")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

account = BankAccount("Jack", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print(account.balance)
```

**Try modifying the starting balance and amounts.**

---

## Step 4: Dunder (magic) methods

Python uses `__double_underscore__` methods to make your objects work with built-in syntax.

```python
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

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)           # uses __repr__
print(v1 + v2)      # uses __add__
print(v1 == Vector(1, 2))   # uses __eq__
```

**What you should see:** `Vector(1, 2)`, `Vector(4, 6)`, `True`

Without `__repr__`, printing an object shows something ugly like `<__main__.Vector object at 0x10a3b2c10>`. Always define it.

---

## Step 5: Class attributes vs instance attributes

```python
class Counter:
    total = 0    # class attribute — shared by ALL instances

    def __init__(self, name):
        self.name = name         # instance attribute — unique per object
        Counter.total += 1

a = Counter("a")
b = Counter("b")
c = Counter("c")

print(Counter.total)   # 3 — class level
print(a.total)         # 3 — Python looks it up on the class
print(a.name)          # "a" — instance level
print(b.name)          # "b"
```

---

## Step 6: Inheritance

A subclass inherits everything from its parent and can override methods.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"

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
    print(f"{animal} says: {animal.speak()}")
```

**What you should see:** Each animal uses its own `speak()` method. This is called **polymorphism** — same method call, different behavior per type.

---

## Now try it yourself

Build a `Rectangle` class:
- `__init__(self, width, height)`
- `area()` — returns width × height
- `perimeter()` — returns 2 × (width + height)
- `__repr__` — returns `"Rectangle(4 x 5)"`
- `is_square()` — returns True if width == height

```python
r = Rectangle(4, 5)
print(r)              # Rectangle(4 x 5)
print(r.area())       # 20
print(r.perimeter())  # 18
print(r.is_square())  # False

s = Rectangle(3, 3)
print(s.is_square())  # True
```
