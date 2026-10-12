This should remove duplicates while keeping the first occurrence of each item in its original order, but the output order is wrong. Explain and fix `dedupe(items)`.

```python
def dedupe(items):
    return list(set(items))
```