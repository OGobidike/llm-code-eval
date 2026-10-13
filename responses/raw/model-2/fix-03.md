### Why it never finishes

The provided binary search enters an infinite loop because the search space is not strictly reduced in every iteration. 

Specifically, when you update the bounds using `lo = mid` or `hi = mid`, the distance between `lo` and `hi` might not shrink. 

**Example of failure:**
Consider `nums = [1, 2]` and `target = 2`.
1. Initially, `lo = 0`, `hi = 1`.
2. `mid = (0 + 1) // 2 = 0`.
3. `nums[0]` is `1`, which is less than `target` (`2`).
4. The code executes `lo = mid`, so `lo` becomes `0`.
5. The state is now exactly the same as step 1 (`lo = 0`, `hi = 1`), and the loop repeats forever.

### The Fix

To guarantee that the search space shrinks on every iteration, you must exclude the `mid` element from the next search space once you've determined it is not the target. 
- If `nums[mid] < target`, the target must be to the right of `mid`, so set `lo = mid + 1`.
- If `nums[mid] > target`, the target must be to the left of `mid`, so set `hi = mid - 1`.

### Fixed Code

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1  # Exclude mid, search right half
        else:
            hi = mid - 1  # Exclude mid, search left half
    return -1
```

### Why this works:
- **Progress is guaranteed:** Because `lo` becomes `mid + 1` or `hi` becomes `mid - 1`, the range `hi - lo` strictly decreases by at least 1 in every iteration.
- **Empty list handling:** If `nums` is empty, `len(nums) - 1` is `-1`. The condition `0 <= -1` is immediately `False`, correctly returning `-1`.
- **Complexity:** The time complexity remains $O(\log n)$ and space complexity is $O(1)$.