The time complexity is $O(|b| + |a|^2)$ in the worst case, and yes, it can be made faster — to $O(|a| + |b|)$ on average.

## 1. Why is the current function $O(|b| + |a|^2)$?

Your function has three main operations:

python
```
seen = set(b)
```

Building a set from `b` takes $O(|b|)$ on average.

python
```
if x in seen
```

Set membership takes $O(1)$ on average, so checking every element of `a` costs $O(|a|)$ in total.

The bottleneck is here:

python
```
x not in out
```

Because `out` is a list, checking whether `x` is already present requires scanning its elements. That costs $O(k)$ when `out` contains $k$ elements.

If all elements of `a` are distinct and appear in `b`, the checks cost approximately

$$
1 + 2 + 3 + \cdots + (|a|-1)
= \frac{|a|(|a|-1)}{2}
= O(|a|^2)
$$

So the overall average-case complexity is:

$$
\boxed{O(|b| + |a|^2)}
$$

Here, $|a|$ and $|b|$ denote the lengths of the two input sequences.

## 2. A faster implementation

Use a second set to track which elements have already been added to the output.

python
```
def common(a, b):
    seen = set(b)
    added = set()
    out = []

    for x in a:
        if x in seen and x not in added:
            out.append(x)
            added.add(x)

    return out
```

This preserves the original behavior:

- Returns elements that occur in both `a` and `b`.
- Removes duplicates from the result.
- Preserves the order of their first appearance in `a`.

The key difference is that `x not in added` is an average-case $O(1)$ set lookup rather than an $O(k)$ list scan.

### New time complexity

| Operation | Average-case cost |
| --- | --- |
| Build `seen` from `b` | $O(\|b\|)$ |
| Iterate through `a` | $O(\|a\|)$ |
| Membership checks and set insertions | $O(\|a\|)$ total |
| Append to `out` | $O(\|a\|)$ total |

Therefore,

$$
\boxed{O(|a| + |b|)}
$$

This is a significant improvement for large inputs.

## 3. Can it be faster still?

The linear-time solution is asymptotically optimal for arbitrary inputs in the usual setting: you generally need to inspect both sequences to determine their intersection.

You could make a small improvement by checking membership in `seen` first, as the code already does. This avoids checking or adding to `added` when an element isn't in `b`.

One subtlety: Python set operations have average-case $O(1)$ complexity, not guaranteed worst-case $O(1)$. Hash collisions can make operations slower in pathological cases.

### Space complexity

The optimized version uses:

- `seen`: $O(|b|)$
- `added`: $O(u)$, where $u$ is the number of unique elements in the output
- `out`: $O(u)$

Total auxiliary and output space is $O(|b| + u)$, or $O(|a| + |b|)$ in the worst case.

One important assumption: Elements in both inputs must be hashable, since they're stored in sets. Your original implementation also requires elements of `b` to be hashable, but the optimized version additionally requires elements of `a` to be hashable.

Bottom line: Replace the list membership check with a set membership check. You retain the output's order and uniqueness while improving the average-case time complexity from quadratic in `a` to linear in both inputs.