

# Gold rewrite: exp-02

**Time complexity: O(m + n·k)**, where n = len(a), m = len(b), and
k = len(out), the number of distinct common items. In the worst case k
grows with n, so it's O(m + n²).

Line by line:
- `seen = set(b)` visits every item of `b` once: O(m).
- `for x in a` runs n times.
- `x in seen` is a set lookup: O(1) on average.
- `x not in out` scans the list `out` item by item: up to O(k) each time.
  This is the slow part.

**Yes, it can be faster.** Track the results in a set as well:

```python
def common(a, b):
    seen = set(b)
    out = []
    added = set()
    for x in a:
        if x in seen and x not in added:
            out.append(x)
            added.add(x)
    return out
```

This runs in O(n + m), because `x not in added` is now a set lookup, O(1),
instead of a scan of the list. The list `out` still keeps the original order.

Changed from the original: added the reason the faster version works (the
membership check moves from a list to a set) and a one-line takeaway.
