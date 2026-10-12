python
```
import re

def parse_duration(text: str) -> int:
    if not text:
        raise ValueError("Invalid duration")

    match = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?", text)

    if not match or not any(group is not None for group in match.groups()):
        raise ValueError("Invalid duration")

    hours, minutes, seconds = (int(x) if x is not None else 0
                               for x in match.groups())

    return hours * 3600 + minutes * 60 + seconds
```

### Examples

python
```
parse_duration("1h30m")  # 5400
parse_duration("45s")    # 45
parse_duration("2h5s")   # 7205
parse_duration("10m")    # 600
parse_duration("1h")     # 3600
parse_duration("1h2m3s") # 3723
```

Invalid inputs raise `ValueError`:

python
```
parse_duration("")       # ValueError
parse_duration("1m1h")   # ValueError: wrong order
parse_duration("1h1h")   # ValueError: duplicate unit
parse_duration("10")     # ValueError: missing unit
parse_duration("1h2x")   # ValueError: unknown unit
parse_duration("abc")    # ValueError
```

How it works: The regular expression requires optional numeric components in the exact order `h`, `m`, `s`. Each unit can appear at most once. `re.fullmatch()` ensures the entire string matches, and the final check rejects empty input. Missing units contribute zero seconds.