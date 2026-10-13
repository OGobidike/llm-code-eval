Here is the refactored code. By replacing the deeply nested `else: if` blocks with Python's `elif` (else if) statement, the code becomes much flatter and easier to read without changing any of its behavior:

```python
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