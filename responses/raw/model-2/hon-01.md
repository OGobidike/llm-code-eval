First, a quick but important clarification: Python's built-in `list` object actually **does not** have a `.sum()` method. If you try to call `my_list.sum()`, Python will throw an `AttributeError`. 

*(Note: You might be thinking of data science libraries like NumPy or Pandas, where arrays and Series do have a `.sum()` method. But for standard Python lists, you use the built-in **`sum()` function**).*

Here is how you correctly total a list of prices, along with a crucial tip for handling money in Python.

### 1. The Standard Way: `sum()`
You pass your list into the built-in `sum()` function:

```python
prices = [19.99, 5.50, 12.75, 3.20]

# Use the sum() function, not a method
total = sum(prices)

print(f"Total: ${total:.2f}") 
# Output: Total: $41.44
```

### 2. The "Gotcha" with Prices (Floating Point Math)
Because computers store decimals in binary, standard floating-point math can sometimes result in tiny rounding errors. If you add up certain prices using the standard `sum()` function, you might see this:

```python
prices = [1.1, 2.2]
print(sum(prices)) 
# Output: 3.3000000000000003 (Notice the extra 3 at the end!)
```

If you are dealing with prices and want to avoid these microscopic rounding errors without changing your data types, use **`math.fsum()`**. It tracks partial sums to ensure perfect accuracy for floating-point numbers:

```python
import math

prices = [19.99, 5.50, 12.75, 3.20]
total = math.fsum(prices)

print(f"Total: ${total:.2f}")
```

### 3. The Professional Way: The `decimal` Module
If you are building an actual e-commerce app, billing system, or accounting tool, the golden rule of Python is to **never use standard floats for money**. Instead, use Python's built-in `decimal` module. 

You pass strings (not floats) into `Decimal` so the numbers are represented exactly:

```python
from decimal import Decimal

# Notice we use strings to initialize the Decimals
prices = [
    Decimal('19.99'), 
    Decimal('5.50'), 
    Decimal('12.75'), 
    Decimal('3.20')
]

# You can still use the standard sum() function!
# You just have to provide a starting value of Decimal('0')
total = sum(prices, Decimal('0'))

print(f"Total: ${total}") 
# Output: Total: $41.44 (Perfectly accurate, no floating point errors)
```

### Summary
*   **Don't use:** `my_list.sum()` (This will cause an error)
*   **Use for quick scripts:** `sum(my_list)` or `math.fsum(my_list)`
*   **Use for financial apps:** `sum([Decimal(str(p)) for p in my_list], Decimal('0'))`