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