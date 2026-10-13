### The Bug
The function crashes with a `ZeroDivisionError` when an empty list is passed to it. 

### Explanation
When `nums` is an empty list (`[]`), the `for` loop doesn't execute, and `total` remains `0`. The function then attempts to evaluate `total / len(nums)`. Since the length of an empty list is `0`, Python attempts to perform division by zero (`0 / 0`), which raises a `ZeroDivisionError` and crashes the program. 

To fix this, we need to add a condition to check if the list is empty before attempting the division, and return `None` as specified.

### Fixed Function
```python
def average(nums):
    if not nums:  # Checks if the list is empty
        return None
    
    total = 0
    for n in nums:
        total += n
        
    return total / len(nums)
```