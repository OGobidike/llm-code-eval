The most Pythonic and efficient way is to use `str.join()` with a generator expression:

python
```
def csv_line(values):
    return ",".join(str(value) for value in values)
```

### Why this is better

- More Pythonic: Uses `join()`, the standard way to combine strings with a delimiter.
- More efficient: Avoids repeatedly creating new strings inside a loop.
- Simpler: Eliminates manual index tracking and comma handling.
- Same return value: Converts each element to a string and separates the elements with commas.

### Example

python
```
print(csv_line([1, "hello", 3.14]))
# 1,hello,3.14

print(csv_line([]))
# ""

print(csv_line([42]))
# 42
```

This preserves the original function's behavior for lists and other iterables, including empty inputs.