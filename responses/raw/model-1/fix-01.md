The bug is that `len(nums)` can be `0` when the list is empty, causing a `ZeroDivisionError` when the function tries to divide by zero.

## Fixed function

python
```
def average(nums):
    if not nums:
        return None

    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```

## Explanation

- `if not nums:` checks whether the list is empty.
- If it is empty, the function returns `None` immediately.
- Otherwise, it sums the numbers and divides by the number of elements, as before.

## Examples

python
```
print(average([2, 4, 6]))  # 4.0
print(average([1, 2]))     # 1.5
print(average([]))         # None
```

Key fix: Check for an empty list before dividing by its length.