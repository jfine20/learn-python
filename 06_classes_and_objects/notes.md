# Classes & Objects — What `self` Really Is

## An object is a bundle of data + behavior

A class is a blueprint. An object (instance) is the actual thing created from it.

```python
class Dog:
    def bark(self):
        print("Woof!")

rex = Dog()   # rex is an instance of Dog
rex.bark()    # "Woof!"
```

## `self` is just the instance

When you call `rex.bark()`, Python translates it to `Dog.bark(rex)`.
`self` is just the name for "the instance this method was called on."
It has no magic — you could name it anything (but don't).

```python
class Dog:
    def __init__(self, name):   # called automatically when you create an instance
        self.name = name        # self.name is an attribute stored ON the object

rex = Dog("Rex")
print(rex.name)  # "Rex"
```

## `__init__` is not the constructor

`__init__` is the *initializer* — it runs after the object is created.
`__new__` is the actual constructor (you rarely need to touch it).

## Instance vs class attributes

```python
class Counter:
    count = 0           # class attribute — shared across ALL instances

    def __init__(self):
        self.value = 0  # instance attribute — unique per instance

a = Counter()
b = Counter()
Counter.count += 1      # affects both a and b
a.value = 5             # only affects a
```

## Dunder (magic) methods

Python uses `__dunder__` methods to make objects work with built-in syntax:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):          # what shows in the REPL / str()
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):    # makes `v1 + v2` work
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):           # makes len(v) work
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
```

## Inheritance

A subclass inherits everything from its parent and can override it.

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):        # override
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
```
