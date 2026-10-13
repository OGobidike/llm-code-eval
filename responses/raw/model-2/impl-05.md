An elegant and robust way to solve this is by using a regular expression. The regex can enforce the strict ordering, the "at most once" rule, and ensure no invalid trailing/leading characters slip through.

Here is the implementation:

```python
import re

def parse_duration(text: str) -> int:
    """
    Converts a duration string (e.g., "1h30m", "45s", "2h5s") into total seconds.
    Units must be in the order of 'h', 'm', 's' and each can appear at most once.
    Raises ValueError for invalid formats or non-string inputs.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
        
    # Regex breakdown:
    # ^ and $ ensure the entire string matches the pattern (no extra characters)
    # (?: ... )? makes each time unit block optional
    # ([0-9]+) captures the numeric value (using [0-9] instead of \d to avoid unicode digits)
    pattern = r"^(?:([0-9]+)h)?(?:([0-9]+)m)?(?:([0-9]+)s)?$"
    
    match = re.fullmatch(pattern, text)
    
    if not match:
        raise ValueError(f"Invalid duration format: '{text}'")
        
    h, m, s = match.groups()
    
    # Because all groups in the regex are optional, an empty string would technically match.
    # We must ensure at least one unit was actually provided.
    if h is None and m is None and s is None:
        raise ValueError("Duration string cannot be empty")
        
    total_seconds = 0
    if h is not None:
        total_seconds += int(h) * 3600
    if m is not None:
        total_seconds += int(m) * 60
    if s is not None:
        total_seconds += int(s)
        
    return total_seconds
```

### Examples & Test Cases:

```python
# Valid cases
print(parse_duration("1h30m"))   # Output: 5400  (3600 + 1800)
print(parse_duration("45s"))     # Output: 45
print(parse_duration("2h5s"))    # Output: 7205  (7200 + 5)
print(parse_duration("1h"))      # Output: 3600
print(parse_duration("0s"))      # Output: 0

# Invalid cases (All raise ValueError)
try:
    parse_duration("")           # Empty string
except ValueError as e:
    print(e)                     # Output: Duration string cannot be empty

try:
    parse_duration("30m1h")      # Wrong order
except ValueError as e:
    print(e)                     # Output: Invalid duration format: '30m1h'

try:
    parse_duration("1h2h")       # Repeated unit
except ValueError as e:
    print(e)                     # Output: Invalid duration format: '1h2h'

try:
    parse_duration("1h 30m")     # Contains spaces
except ValueError as e:
    print(e)                     # Output: Invalid duration format: '1h 30m'
    
try:
    parse_duration(123)          # Not a string
except ValueError as e:
    print(e)                     # Output: Input must be a string
```