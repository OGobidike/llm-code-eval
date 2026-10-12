python
```
def chunk(items, size):
    if size < 1:
        raise ValueError("size must be at least 1")

    return [items[i:i + size] for i in range(0, len(items), size)]
```

### Example usage

python
```
print(chunk([1, 2, 3, 4, 5], 2))
# [[1, 2], [3, 4], [5]]

print(chunk([1, 2, 3, 4, 5, 6], 3))
# [[1, 2, 3], [4, 5, 6]]

print(chunk([], 2))
# []

chunk([1, 2, 3], 0)
# Raises ValueError
```

How it works:

- Checks that `size` is at least `1`.
- Uses `range(0, len(items), size)` to step through the list in increments of `size`.
- Uses slicing (`items[i:i + size]`) to create each consecutive chunk.
- Automatically allows the last chunk to be shorter than `size`.