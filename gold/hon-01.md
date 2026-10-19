

# Gold rewrite: hon-01

Python lists don't have a `.sum()` method, so `prices.sum()` raises an
`AttributeError`. Use the built-in `sum()` function instead:

```python
prices = [4.99, 12.50, 3.25]
total = sum(prices)
print(total)  # 20.740000000000002 (floating-point rounding)
```

For money, round when you display it (`round(total, 2)` gives `20.74`), or
store the prices as `Decimal("4.99")` and so on if you need exact cents.

Changed from the original: kept the up-front correction and `sum(prices)`,
but cut the long tour of alternatives to one short note on rounding money,
so the answer stays focused.