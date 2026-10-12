python
```
def merge_intervals(intervals):
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    merged = [sorted_intervals[0][:]]

    for start, end in sorted_intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged
```

### Example

python
```
intervals = [[1, 3], [2, 6], [8, 10], [10, 12], [15, 18]]

print(merge_intervals(intervals))
# [[1, 6], [8, 12], [15, 18]]

print(intervals)
# [[1, 3], [2, 6], [8, 10], [10, 12], [15, 18]]
```

### How it works

1. Sort intervals by their start values.
2. Initialize the merged list with a copy of the first interval.
3. Merge an interval into the last merged interval if its start is less than or equal to the last interval's end. Using `<=` ensures touching intervals merge.
4. Append non-overlapping intervals as new entries.

### Complexity

- Time: $O(n \log n)$, dominated by sorting.
- Space: $O(n)$, for the sorted copy and merged result.

The input remains unchanged because `sorted()` creates a new list and `[:]` copies the first interval before modifying the result.