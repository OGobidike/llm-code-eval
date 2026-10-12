Make this function more Pythonic and efficient without changing what it returns. Keep the name `csv_line(values)`.

```python
def csv_line(values):
    line = ""
    for i in range(len(values)):
        line = line + str(values[i])
        if i != len(values) - 1:
            line = line + ","
    return line
```