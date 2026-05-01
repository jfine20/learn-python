# Modules — How `import` Actually Works

## A module is just a file

Any `.py` file is a module. When you `import` it, Python runs the file
top-to-bottom and makes its names available.

```python
# math_utils.py
PI = 3.14159

def circle_area(r):
    return PI * r * r
```

```python
import math_utils
print(math_utils.PI)
print(math_utils.circle_area(5))
```

## How Python finds modules

When you write `import foo`, Python searches:
1. The current directory (or the directory of the running script)
2. Directories in `sys.path` (includes the standard library and installed packages)
3. The standard library

```python
import sys
print(sys.path)  # see where Python looks
```

## Import styles

```python
import os                      # import the module — access with os.path
from os import path            # import one name — access with path
from os import path as p       # aliased
from os import *               # import everything — avoid this
```

`from module import *` pollutes your namespace and makes it impossible to
tell where a name came from. Don't use it.

## `if __name__ == "__main__"`

When Python runs a file directly, `__name__` is `"__main__"`.
When a file is imported, `__name__` is the module's name.

This lets you write code that only runs when the file is executed directly:

```python
def greet(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
    greet("World")   # only runs when you do `python myfile.py`
                     # NOT when another file does `import myfile`
```

## The standard library — things you get for free

Python ships with a huge standard library. Know these:

| Module | What it does |
|--------|-------------|
| `os` | OS operations — paths, env vars, directories |
| `sys` | Python runtime — `sys.argv`, `sys.path`, `sys.exit` |
| `json` | Serialize/deserialize JSON |
| `datetime` | Dates and times |
| `pathlib` | Modern file paths (better than os.path) |
| `collections` | Counter, defaultdict, deque |
| `itertools` | Lazy iterators — chain, product, groupby |
| `functools` | Higher-order functions — lru_cache, partial, reduce |
| `re` | Regular expressions |
| `math` | Math functions |

## Packages

A package is a folder with an `__init__.py` file. It lets you organize
modules into a hierarchy:

```
myproject/
    __init__.py
    utils.py
    models/
        __init__.py
        user.py
```

`from myproject.models.user import User`
