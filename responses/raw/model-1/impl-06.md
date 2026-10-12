python
```
def flatten(nested):
    result = []

    for item in nested:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result
```

### Example usage

python
```
print(flatten([1, [2, (3, "ab")], [[4]]]))
# Output: [1, 2, 3, 'ab', 4]
```

### How it works

- Iterates through each item in the input.
- Recursively flattens items that are lists or tuples.
- Appends everything else as a single element, so strings like `"ab"` remain intact.
- Preserves order by processing elements from left to right.

This works for arbitrarily deep nesting, provided the nested lists and tuples do not contain cycles.