This binary search sometimes never finishes. Explain why and give a fixed `binary_search(nums, target)` that returns the index of `target` in the sorted list `nums`, or -1.

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid
        else:
            hi = mid
    return -1
```