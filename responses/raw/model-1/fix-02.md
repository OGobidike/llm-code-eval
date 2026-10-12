The issue is that Python evaluates default argument values only once, when the function is defined. So, the same list `[]` is reused across calls, causing tags from previous calls to persist.

### Fixed code

Use `None` as the default and create a new list inside the function:

python
```
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
```

### Example

python
```
print(add_tag("python"))  # ['python']
print(add_tag("coding"))  # ['coding']
```

Each call without `tags` now starts with a fresh, empty list.

Why this works: `None` is immutable and safe to use as a default. Initializing `tags = []` inside the function ensures a new list is created whenever the caller doesn't provide one.

Note that explicitly passing a list still works as expected:

python
```
my_tags = ["beginner"]
print(add_tag("python", my_tags))  # ['beginner', 'python']
```