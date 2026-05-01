# Error Handling — Exceptions as Control Flow

## Exceptions are objects

An exception is just an object that inherits from `BaseException`.
When you `raise` one, Python unwinds the call stack looking for a matching `except`.

```python
class MyError(Exception):
    pass

raise MyError("something went wrong")
```

## The exception hierarchy

```
BaseException
├── SystemExit           ← sys.exit() raises this
├── KeyboardInterrupt    ← Ctrl+C
└── Exception            ← almost everything you'll catch
    ├── ValueError       ← right type, wrong value ("abc" can't be an int)
    ├── TypeError        ← wrong type entirely
    ├── KeyError         ← dict key doesn't exist
    ├── IndexError       ← list index out of range
    ├── AttributeError   ← object doesn't have that attribute
    ├── FileNotFoundError
    └── ...
```

Never catch `BaseException` — it swallows `SystemExit` and `KeyboardInterrupt`.
Catch `Exception` or a specific subclass.

## try / except / else / finally

```python
try:
    result = int("abc")
except ValueError as e:
    print(f"Conversion failed: {e}")
else:
    print(f"Got: {result}")   # runs only if NO exception was raised
finally:
    print("Always runs")      # cleanup — runs no matter what
```

## Raise early, catch late

Raise exceptions close to where the problem is.
Catch them as high up as makes sense — where you can actually do something about it.

```python
def parse_age(s):
    age = int(s)           # raises ValueError if s isn't a number
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age
```

## Don't use exceptions for flow control you expect

```python
# BAD — using exceptions as if/else
try:
    value = my_dict["key"]
except KeyError:
    value = "default"

# GOOD
value = my_dict.get("key", "default")
```

Use exceptions for *unexpected* failures, not for outcomes you anticipate.
