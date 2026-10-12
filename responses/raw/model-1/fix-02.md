Calling this function twice gives surprising results: the second call's list still contains the first call's tag. Explain why, and fix `add_tag` so each call without `tags` starts from an empty list.

```python
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags
```