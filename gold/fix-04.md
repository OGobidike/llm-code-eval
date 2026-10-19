

# Gold rewrite: fix-04

The error happens because the loop walks over `stock` while `del` removes keys
from it. Python doesn't allow a dict to change size during iteration, because
the loop would lose its place.

Loop over a snapshot of the keys instead, and delete from the real dict:

```python
def remove_low_stock(stock, minimum):
    for item in list(stock):
        if stock[item] < minimum:
            del stock[item]
    return stock
```

`list(stock)` copies the keys before the loop starts, so deleting is safe.
The dict is changed in place and returned, so the caller gets back the same
object they passed in, as the prompt asks.

Changed from the original: removed the dict-comprehension alternative, which
returned a new dict and broke the "returns the same dict" requirement; kept
only the in-place fix.
