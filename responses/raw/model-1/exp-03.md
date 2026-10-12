In Python, `==` checks whether two objects have equal values, while `is` checks whether two references point to the exact same object.

## 1. The difference

- `==` → Do these objects have the same value?
- `is` → Are these the very same object in memory?

## 2. An example where they disagree

python
```
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```

Why?

- `a == b` is `True` because both lists contain the same elements.
- `a is b` is `False` because Python created two separate list objects.

Here's a case where both are `True`:

python
```
a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True
```

Here, `b = a` makes `b` refer to the same list as `a`.

## 3. When should you use `is`?

Use `is` when you want to check object identity, especially when comparing against `None`.

python
```
result = None

if result is None:
    print("No result available")
```

This is the recommended Python style. You can also write:

python
```
if result is not None:
    print("A result is available")
```

Use `==` for ordinary value comparisons:

python
```
age = 18

if age == 18:
    print("You are 18")
```

Avoid using `is` to compare strings, numbers, or other values. Python sometimes reuses objects internally, so identity checks on values can behave unexpectedly.

For example, use `a == b` to compare two strings' contents, not `a is b`.

## Quick rule to remember

| Operator | Meaning | Typical use |
| --- | --- | --- |
| `==` | Equal values | Numbers, strings, lists, and other value comparisons |
| `is` | Same object | `None` checks and intentional identity checks |

In short: Use `==` to compare values and `is` to compare identity.