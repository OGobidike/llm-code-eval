python
```
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

What changed:

- Replaced nested `else` blocks with `elif` statements.
- Removed unnecessary indentation to improve readability.
- Kept the function name, return values, and evaluation order unchanged.