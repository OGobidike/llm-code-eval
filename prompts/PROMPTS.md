# The prompts

Paste each prompt, exactly as written, into a **new chat** with each model.

## impl-01 (implement, hidden tests)

Write a Python function `chunk(items, size)` that splits a list into consecutive sublists of length `size`; the last chunk may be shorter. If `size` is less than 1, raise `ValueError`. Example: `chunk([1, 2, 3, 4, 5], 2)` returns `[[1, 2], [3, 4], [5]]`.

## impl-02 (implement, hidden tests)

Write a Python function `merge_intervals(intervals)` that takes a list of `[start, end]` pairs in any order and returns the merged, sorted list. Intervals that touch, like `[1, 3]` and `[3, 5]`, should merge. Don't modify the input list.

## impl-03 (implement, hidden tests)

Write a Python function `is_anagram(a, b)` that returns True if the two strings are anagrams of each other, ignoring case and spaces. For example, `is_anagram("Dormitory", "dirty room")` is True.

## impl-04 (implement, hidden tests)

Write a Python function `longest_unique_substring(s)` that returns the length of the longest substring of `s` with no repeated characters. It should run in O(n) time. Explain your approach in two or three sentences.

## impl-05 (implement, hidden tests)

Write a Python function `parse_duration(text)` that converts strings like "1h30m", "45s" or "2h5s" into a total number of seconds (an int). Units are h, m and s, each used at most once and in that order. Raise `ValueError` for anything else, including an empty string.

## impl-06 (implement, hidden tests)

Write a Python function `flatten(nested)` that flattens arbitrarily nested lists and tuples into a single flat list, keeping order. Strings must not be split into characters. Example: `flatten([1, [2, (3, "ab")], [[4]]])` returns `[1, 2, 3, "ab", 4]`.

## fix-01 (bug-fix, hidden tests)

This function should return the average of a list of numbers, or None for an empty list, but it crashes. Find the bug, explain it, and give the fixed function.

```python
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```

## fix-02 (bug-fix, hidden tests)

Calling this function twice gives surprising results: the second call's list still contains the first call's tag. Explain why, and fix `add_tag` so each call without `tags` starts from an empty list.

```python
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags
```

## fix-03 (bug-fix, hidden tests)

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

## fix-04 (bug-fix, hidden tests)

This raises `RuntimeError: dictionary changed size during iteration`. Explain why and fix `remove_low_stock(stock, minimum)` so it removes every item whose quantity is below `minimum` and returns the same dict.

```python
def remove_low_stock(stock, minimum):
    for item in stock:
        if stock[item] < minimum:
            del stock[item]
    return stock
```

## fix-05 (bug-fix, hidden tests)

This should remove duplicates while keeping the first occurrence of each item in its original order, but the output order is wrong. Explain and fix `dedupe(items)`.

```python
def dedupe(items):
    return list(set(items))
```

## ref-01 (refactor, hidden tests)

Refactor this for readability without changing its behavior. Keep the name `letter_grade(score)`.

```python
def letter_grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"
```

## ref-02 (refactor, hidden tests)

Make this function more Pythonic and efficient without changing what it returns. Keep the name `csv_line(values)`.

```python
def csv_line(values):
    line = ""
    for i in range(len(values)):
        line = line + str(values[i])
        if i != len(values) - 1:
            line = line + ","
    return line
```

## exp-01 (explain, graded by reading)

Why does this print `None` instead of the sorted list? What should I use instead, and when would I choose each option?

```python
nums = [3, 1, 2]
result = nums.sort()
print(result)
```

## exp-02 (explain, graded by reading)

What is the time complexity of this function, and why? Could it be faster?

```python
def common(a, b):
    seen = set(b)
    out = []
    for x in a:
        if x in seen and x not in out:
            out.append(x)
    return out
```

## exp-03 (explain, graded by reading)

In Python, what's the difference between `is` and `==`? Give an example where they disagree, and say when `is` is the right choice.

## amb-01 (ambiguous, graded by reading)

Write a function that cleans up phone numbers.

## hon-01 (false-premise, graded by reading)

How do I use Python's built-in `list.sum()` method to total a list of prices?
