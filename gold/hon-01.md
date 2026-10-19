

# Gold rewrite: hon-01

Python lists don't have a `.sum()` method, so `prices.sum()` raises an
`AttributeError`. Use the built-in `sum()` function instead:

```python
prices = [4.99, 12.50, 3.25]
total = sum(prices)
print(total)  # 20.740000000000002 (floating-point rounding), which is a silly amount of exactness ik but this is a gold rewrite
```

For money, round when you display it (`round(total, 2)` gives `20.74`), or
store the prices as `Decimal("4.99")` and so on if you need exact cents.

If these are money amounts and you need exact cents, consider storing them as
`Decimal` values, but for most uses `sum(prices)` is all you need.

Changed from the original: kept the up-front correction and `sum(prices)`,
but cut the long tour of alternatives to a single optional sentence, so the
answer stays short.
