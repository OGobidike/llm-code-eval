This raises `RuntimeError: dictionary changed size during iteration`. Explain why and fix `remove_low_stock(stock, minimum)` so it removes every item whose quantity is below `minimum` and returns the same dict.

```python
def remove_low_stock(stock, minimum):
    for item in stock:
        if stock[item] < minimum:
            del stock[item]
    return stock
```