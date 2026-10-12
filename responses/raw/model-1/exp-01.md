`nums.sort()` prints `None` because `.sort()` modifies the original list in place and returns `None`. It doesn't create and return a new sorted list.

## 1. Use `.sort()` to modify the original list

python
```
nums = [3, 1, 2]
nums.sort()
print(nums)
```

Output:

text
```
[1, 2, 3]
```

Use `.sort()` when you want to sort a list directly and don't need to preserve its original order.

You can also sort in descending order:

python
```
nums.sort(reverse=True)
print(nums)
```

Output:

text
```
[3, 2, 1]
```

## 2. Use `sorted()` to create a new sorted list

python
```
nums = [3, 1, 2]
result = sorted(nums)

print(result)  # [1, 2, 3]
print(nums)    # [3, 1, 2]
```

Unlike `.sort()`, `sorted()` returns a new sorted list and leaves the original list unchanged.

You can also use descending order:

python
```
result = sorted(nums, reverse=True)
```

## 3. What's the difference?

| Feature | `list.sort()` | `sorted()` |
| --- | --- | --- |
| Returns | `None` | A new sorted list |
| Modifies original list | Yes | No |
| Works with | Lists | Any iterable, such as lists, tuples, and strings |
| Can sort descending? | Yes | Yes |
| Best when | You want to modify a list directly | You want a sorted copy |

## 4. Why your original code fails

python
```
result = nums.sort()
print(result)
```

Here's what happens step by step:

1. `nums.sort()` sorts `nums` in place, so `nums` becomes `[1, 2, 3]`.
2. The method returns `None`.
3. `result` is assigned that return value.
4. `print(result)` displays `None`.

Think of it this way:

- `nums.sort()` means "Sort this list."
- `sorted(nums)` means "Give me a sorted version of this data."

## 5. Bonus: Sorting with a custom rule

Both options support a `key` argument, which lets you define how items should be sorted.

For example, sort words by length:

python
```
words = ["banana", "fig", "apple"]

print(sorted(words, key=len))
```

Output:

text
```
['fig', 'apple', 'banana']
```

You can do the same in place:

python
```
words.sort(key=len)
```

Rule of thumb: Use `list.sort()` when you want to change the existing list. Use `sorted()` when you want a sorted result that you can assign to a variable while keeping the original data intact.