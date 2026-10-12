Python lists don’t have a built-in `list.sum()` method. Instead, use Python’s built-in `sum()` function to total a list of prices.

### Example

python
```
prices = [10.99, 25.50, 5.75, 12.00]

total = sum(prices)

print(total)  # 54.24
```

### How it works

- `prices` is a list of prices.
- `sum(prices)` adds all the numbers in the list.
- `total` stores the result.

### Adding a currency symbol

python
```
prices = [10.99, 25.50, 5.75, 12.00]

total = sum(prices)

print(f"Total: ${total:.2f}")
```

Output:

text
```
Total: $54.24
```

The `:.2f` formats the result to two decimal places.

Tip: For financial calculations where exact decimal arithmetic matters, use Python's `decimal.Decimal` rather than floating-point numbers to avoid rounding errors.