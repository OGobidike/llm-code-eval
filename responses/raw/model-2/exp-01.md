### Why it prints `None`

In Python, the `.sort()` method sorts the list **in-place**. This means it modifies the original list directly in memory rather than creating a brand new list. 

By design, Python methods that mutate (change) an object in-place return `None`. This is a deliberate choice by Python's creators to make it explicitly clear that the original object was altered and no new object was created. 

If you print `nums` instead of `result`, you will see that the list was actually sorted:
```python
nums = [3, 1, 2]
nums.sort()
print(nums)    # Output: [1, 2, 3]
```

---

### What to use instead

If you want to assign the sorted result to a new variable, you should use Python's built-in **`sorted()`** function instead:

```python
nums = [3, 1, 2]
result = sorted(nums)
print(result)  # Output: [1, 2, 3]
print(nums)    # Output: [3, 1, 2] (Original list is unchanged)
```

---

### When to choose each option

Here is a breakdown of when you should use `.sort()` versus `sorted()`:

#### 1. Use `list.sort()` when:
* **You want to save memory:** Because it sorts the list in-place, it doesn't need to allocate memory to create a copy of the list. This is highly beneficial if you are working with massive lists.
* **You don't need the original order:** If the original unsorted order of the data is no longer useful to you, mutating it in-place is slightly faster and more efficient.
* **You are chaining operations (rarely):** You just want to sort a list and immediately do something else with that exact same list.

#### 2. Use `sorted()` when:
* **You need to keep the original list intact:** If you need to compare the sorted version against the original unsorted version later, `sorted()` is mandatory because it leaves the original data untouched.
* **You are working with other Iterables:** `.sort()` is a list-only method. `sorted()` works on **any** iterable in Python, including tuples, strings, dictionaries, sets, and generators. (Note: `sorted()` will *always* return a new list, even if you pass it a tuple or a string).
    ```python
    my_tuple = (3, 1, 2)
    # my_tuple.sort()  <-- This would cause an AttributeError
    result = sorted(my_tuple) # This works and returns a list: [1, 2, 3]
    ```
* **You are writing a one-liner:** If you need to pass a sorted list directly into another function, `sorted()` is much cleaner.
    ```python
    # Clean and readable:
    print(sorted([3, 1, 2])) 
    
    # Clunky:
    nums = [3, 1, 2]
    nums.sort()
    print(nums)
    ```

### Summary Rule of Thumb
* Use **`sorted(nums)`** when you want a **new** sorted list and want to keep the original safe.
* Use **`nums.sort()`** when you want to **update** the existing list and want to save memory.