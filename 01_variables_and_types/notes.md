# Variables & Types — What Things Actually Mean

## A variable is NOT a box

In many languages, a variable is like a box: you put a value in it.

In Python, a variable is a **name tag** attached to an object. The object exists
independently in memory. The name just points to it.

```python
x = 5
y = x
x = 10

print(y)  # still 5 — y points to the original 5 object, not to x
```

This matters enormously when the object is mutable (changeable):

```python
a = [1, 2, 3]
b = a          # b is another name tag for the SAME list
a.append(4)

print(b)       # [1, 2, 3, 4] — b "saw" the change because it's the same object
```

Use `id()` to see the object's memory address:

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # True — same object
```

## Types live on objects, not variables

Python is *dynamically typed*: the name tag has no type. The object it points to does.

```python
x = 5        # x → int object
x = "hello"  # x → str object (the int is untouched in memory until garbage collected)
```

Check type with `type()` or `isinstance()`:

```python
type(5)         # <class 'int'>
isinstance(5, int)  # True
```

## Mutable vs immutable

**Immutable** — the object can never change after creation:
`int`, `float`, `str`, `tuple`, `bool`

**Mutable** — the object can be changed in-place:
`list`, `dict`, `set`

This is why strings feel like they "change" but don't:

```python
s = "hello"
s = s + " world"  # a brand new string object is created; "hello" is untouched
```

## None

`None` is Python's way of saying "no value." It's an object too — there's only one
`None` in existence. Always check with `is`, not `==`:

```python
x = None
if x is None:
    print("nothing here")
```
