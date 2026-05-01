# Module 1: Variables & Types (deeper)

## You already know what a variable is — now let's go deeper

In Module 0 you learned that variables store values. Now we're going to look at **how Python actually stores things in memory**, because understanding this will save you from confusing bugs later.

Most people are taught that a variable is like a **box** — you put a value inside it. That works as a beginner mental model, but it's wrong in Python, and it will confuse you later.

In Python, a variable is a **name tag**. The object (the actual value) lives somewhere in memory. The variable is just a label you stick on it.

---

## Step 1: Create your first variable

Type this in the editor and press **Run**:

```python
x = 5
print(x)
```

**What you should see:** `5`

The `=` sign doesn't mean "equals" like in math. It means **"attach the name `x` to the object `5`"**.

---

## Step 2: See why name tags matter

Now try this:

```python
a = [1, 2, 3]
b = a
a.append(99)
print(a)
print(b)
```

**What you should see:** Both `a` and `b` print `[1, 2, 3, 99]`.

**Why?** Because `b = a` doesn't copy the list. It creates a second name tag pointing to the **same list**. So when you change the list through `a`, `b` also sees the change — they're looking at the same object.

---

## Step 3: Prove it with id()

`id()` shows you the memory address of an object — its unique identity.

```python
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))
```

**What you should see:** Both ids are identical. `True` at the end.

Now try making a real copy:

```python
a = [1, 2, 3]
b = a.copy()
a.append(99)
print(a)
print(b)
print(id(a) == id(b))
```

**What you should see:** `a` has 99, `b` doesn't. `False` — different objects.

---

## Step 4: Mutable vs Immutable

Some objects **can** be changed after creation. Some **cannot**.

- **Immutable** (can't change): `int`, `float`, `str`, `tuple`, `bool`
- **Mutable** (can change): `list`, `dict`, `set`

Try this to see strings are immutable:

```python
s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print("Error:", e)
```

**What you should see:** An error saying you can't assign to a string.

Now try this — it *looks* like you changed the string, but you didn't:

```python
s = "hello"
print(id(s))
s = s + " world"
print(id(s))
```

**What you should see:** Two different ids. `s` now points to a **brand new string object**. The original `"hello"` was never touched.

---

## Step 5: Types

Every object has a type. The variable itself has no type — only the object it points to does.

```python
thing = 42
print(type(thing))

thing = "now a string"
print(type(thing))

thing = [1, 2, 3]
print(type(thing))
```

**What you should see:** The type changes each time, but `thing` is just a name tag pointing to whatever object you give it.

---

## Step 6: None

`None` means "no value". It's Python's way of saying "nothing here."

```python
result = None
print(result)
print(type(result))

if result is None:
    print("nothing here")
```

Always use `is None` to check for None — not `== None`. There's only one `None` object in all of Python, so `is` (identity check) is the right tool.

---

## Now experiment

Try changing the code. Some ideas:
- What happens if you do `x = 5` then `y = x` then `x = 10` — what is `y`?
- What happens if you put a list inside a list and copy it?
- Can you put different types in the same list?
