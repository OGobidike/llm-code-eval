

# Gold rewrite: impl-02

```python
def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

Sort the intervals by start, then walk through them once: if an interval
overlaps or touches the last merged one (`<=`), extend that one's end;
otherwise start a new interval. Each merged interval is a new `[start, end]`
list, so the caller's input is never modified.

Changed from the original: appends a new `[start, end]` list instead of the
caller's interval, so extending `merged[-1][1]` can no longer change the input.
