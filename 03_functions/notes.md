# Functions — What They Actually Are

## Functions are objects

In Python, a function is just an object — like a list or a string. You can
pass it around, store it in a variable, put it in a list.

```python
def greet(name):
    return f"Hello, {name}"

say_hi = greet          # say_hi now points to the same function object
print(say_hi("Jack"))   # "Hello, Jack"
```

This is what makes callbacks, decorators, and higher-order functions possible.

## Scope — where Python looks for names (LEGB)

When you use a name, Python searches in this order:
1. **L**ocal — inside the current function
2. **E**nclosing — any outer functions (for closures)
3. **G**lobal — the module level
4. **B**uilt-in — Python's built-ins (len, print, etc.)

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)   # finds "enclosing" (E before G)
    inner()
```

## Default arguments — the gotcha everyone hits

Default values are evaluated ONCE when the function is defined, not each time it's called.

```python
def add_item(item, items=[]):   # BAD — this list is shared across all calls
    items.append(item)
    return items

print(add_item("a"))  # ["a"]
print(add_item("b"))  # ["a", "b"] — NOT ["b"] — same list object reused!
```

The fix:
```python
def add_item(item, items=None):  # GOOD
    if items is None:
        items = []
    items.append(item)
    return items
```

## *args and **kwargs

`*args` collects extra positional arguments into a tuple.
`**kwargs` collects extra keyword arguments into a dict.

```python
def log(*args, **kwargs):
    print(args)    # tuple of positional args
    print(kwargs)  # dict of keyword args

log(1, 2, 3, level="info", color="red")
# (1, 2, 3)
# {'level': 'info', 'color': 'red'}
```

## Return values

Every function returns something. If there's no `return`, it returns `None`.

```python
def do_thing():
    x = 1 + 1   # no return

result = do_thing()
print(result)  # None
```
