This function should return the average of a list of numbers, or None for an empty list, but it crashes. Find the bug, explain it, and give the fixed function.

```python
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```