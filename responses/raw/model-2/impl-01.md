An elegant and Pythonic way to solve this is by using list comprehension combined with list slicing and the `range()` function. 

Here is the implementation:

```python
def chunk(items, size):
    """
    Splits a list into consecutive sublists of a given size.
    
    :param items: The list to be chunked.
    :param size: The maximum size of each chunk.
    :return: A list of sublists.
    """
    if size < 1:
        raise ValueError("Chunk size must be at least 1")
        
    return [items[i:i + size] for i in range(0, len(items), size)]
```

### How it works:
1. **Validation**: It first checks if the `size` is less than `1`. If it is, a `ValueError` is raised as requested.
2. **`range(0, len(items), size)`**: This generates the starting indices for each chunk. For a list of length 5 and a size of 2, it yields `0, 2, 4`.
3. **`items[i:i + size]`**: This uses Python's list slicing to grab a sublist starting at index `i` and ending at `i + size`. If the slice goes past the end of the list, Python safely handles it and just returns the remaining elements (which naturally handles the "last chunk may be shorter" requirement).

### Example Usage:
```python
print(chunk([1, 2, 3, 4, 5], 2)) 
# Output: [[1, 2], [3, 4], [5]]

print(chunk(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3)) 
# Output: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g']]

print(chunk([1, 2, 3], 5)) 
# Output: [[1, 2, 3]]

print(chunk([], 3)) 
# Output: []
```