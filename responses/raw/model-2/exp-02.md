## Time Complexity Analysis

The time complexity of this function is **O(n + m²)**, where:
- `n` = length of `b`
- `m` = length of `a`

### Breakdown:

1. **`seen = set(b)`** → O(n)
   Creating a set from `b` requires iterating through all `n` elements.

2. **`for x in a:`** → O(m) iterations
   The loop runs once for each element in `a`.

3. **`x in seen`** → O(1) average
   Set lookups are constant time on average.

4. **`x not in out`** → **O(k)** where `k` is the current length of `out`
   This is the bottleneck! Checking membership in a **list** requires a linear scan. In the worst case (all elements in `a` are unique and common with `b`), `out` grows to size `m`, making this check O(m) per iteration.

5. **`out.append(x)`** → O(1) amortized

**Total:** O(n) + O(m × m) = **O(n + m²)**

---

## Can It Be Faster?

**Yes!** The problem is using a list for membership testing. You can achieve **O(n + m)** by tracking seen elements with a set:

```python
def common(a, b):
    seen = set(b)
    out = []
    seen_out = set()  # Track what's already in out
    for x in a:
        if x in seen and x not in seen_out:
            out.append(x)
            seen_out.add(x)
    return out
```

Or even more concisely using a **dict** (which preserves insertion order in Python 3.7+):

```python
def common(a, b):
    seen = set(b)
    return list({x: None for x in a if x in seen}.keys())
```

Both optimized versions run in **O(n + m)** time, eliminating the quadratic bottleneck.