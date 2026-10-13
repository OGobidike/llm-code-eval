# The Mutable Default Argument Gotcha

## Why this happens

In Python, **default argument values are evaluated exactly once — when the `def` statement runs**, not each time the function is called. The resulting object is stored on the function itself and reused on every call that omits that argument.

So in your code:

```python
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags
```

The `[]` is created **once** at definition time. Every call that omits `tags` binds the name `tags` to that *same* list object. You can even see it:

```python
>>> add_tag.__defaults__
([],)
>>> add_tag("a")
['a']
>>> add_tag.__defaults__
(['a'],)            # the default has been mutated!
>>> add_tag("b")
['a', 'b']
```

Because lists are mutable, `.append` modifies the shared default in place, so the second call "remembers" the first.

## The fix

Use `None` as a sentinel and build a fresh list inside the function body:

```python
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
```

Now each call without `tags` gets its own new list:

```python
>>> add_tag("a")
['a']
>>> add_tag("b")
['b']
>>> add_tag("c", ["x"])   # explicit list still works
['x', 'c']
```

## The rule of thumb

**Never use a mutable object (`list`, `dict`, `set`, custom instances) as a default argument** unless you explicitly want it to persist across calls. Use `None` and construct the mutable object inside the function. Immutable defaults (`int`, `str`, `tuple`, `None`, `bool`) are safe because they can't be mutated in place.