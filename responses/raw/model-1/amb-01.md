Here’s a Python function that cleans up phone numbers by removing spaces, dashes, parentheses, and other non-digit characters while preserving an optional leading `+`.

python
```
import re

def clean_phone_number(phone: str) -> str:
    """Remove formatting characters from a phone number."""
    phone = phone.strip()
    has_plus = phone.startswith("+")
    digits = re.sub(r"\D", "", phone)

    return f"+{digits}" if has_plus else digits

# Examples
print(clean_phone_number("+1 (234) 567-8900"))  # +12345678900
print(clean_phone_number("234-567-8900"))       # 2345678900
print(clean_phone_number("(123) 456 7890"))     # 1234567890
print(clean_phone_number("+234 803 123 4567"))  # +2348031234567
```

How it works:

- `strip()` removes leading and trailing whitespace.
- `re.sub(r"\D", "", phone)` removes every non-digit character.
- The function preserves a leading `+` for international phone numbers.

Note: This function normalizes formatting but does not validate whether a phone number is real or correctly formatted for a particular country.