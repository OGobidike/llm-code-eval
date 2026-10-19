

# Gold rewrite: amb-01

"Clean up" can mean different things: strip formatting, validate, or reformat,
and phone formats differ by country. I'll assume US/Canada numbers and return
them in the standard `(555) 123-4567` format. If you need another country or
just the digits, tell me and I'll adjust it.

```python
import re


def clean_phone_number(raw):
    digits = re.sub(r"\D", "", raw)          # keep digits only
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]                  # drop the +1 country code
    if len(digits) != 10:
        raise ValueError(f"not a valid 10-digit phone number: {raw!r}")
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
```

- `clean_phone_number("555.123.4567")` returns `"(555) 123-4567"`
- `clean_phone_number("+1 555 123 4567")` returns `"(555) 123-4567"`
- `clean_phone_number("abc")` raises `ValueError`

Changed from the original: flags the ambiguity and states its assumptions up
front, says exactly what it returns, and raises ValueError on bad input
instead of silently returning None.
