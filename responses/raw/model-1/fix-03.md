The problem is that the search boundaries do not move past `mid`. If `mid` is the only remaining candidate, assigning `lo = mid` or `hi = mid` leaves the boundaries unchanged, so the loop can run forever.

For example, with `nums = [3, 5]` and `target = 5`, `lo = 0`, `hi = 1`, and `mid = 0`. Since `nums[0] < target`, the code sets `lo = 0` again. Nothing changes, and the same iteration repeats indefinitely.

## Fixed implementation

python
```
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
```

## Why this works

- If `nums[mid] < target`: All elements at or before `mid` are too small, so set `lo = mid + 1`.
- If `nums[mid] > target`: All elements at or after `mid` are too large, so set `hi = mid - 1`.
- If `nums[mid] == target`: Return `mid` immediately.
- If `lo > hi`: No candidates remain, so return `-1`.

The key fix is using `mid + 1` and `mid - 1`. Each unsuccessful iteration strictly shrinks the search interval, guaranteeing termination.

Complexity:

- Time: $O(\log n)$
- Extra space: $O(1)$

The function assumes `nums` is sorted in ascending order and returns an index of the target if found, or `-1` otherwise.