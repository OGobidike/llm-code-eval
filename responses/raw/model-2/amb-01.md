Because phone number formats vary wildly around the world, "cleaning up" a phone number can mean a few different things. 

Below are the two best ways to do this in **Python**:
1. **The Pure Python (Regex) Approach**: Best for quick scripts, stripping out messy characters, and formatting North American numbers.
2. **The Production-Ready Approach**: Using Google's `phonenumbers` library, which is the industry standard for validating and formatting international numbers.

### Approach 1: Pure Python (Regex)
This function strips out all non-numeric characters, intelligently separates extensions (like `ext. 123`), and formats standard 10-digit US/Canada numbers into a readable `(XXX) XXX-XXXX` format.

```python
import re

def clean_phone_number(phone_str):
    if not phone_str or not isinstance(phone_str, str):
        return None

    # 1. Extract extension if it exists (e.g., "ext. 123", "x123", "#123")
    ext_pattern = re.compile(r'(?:ext\.?|x\.?|#)\s*(\d+)\s*$', re.IGNORECASE)
    ext_match = ext_pattern.search(phone_str)
    
    extension = ext_match.group(1) if ext_match else None
    base_number = phone_str[:ext_match.start()] if ext_match else phone_str

    # 2. Strip all non-digit characters from the base number
    digits_only = re.sub(r'\D', '', base_number)

    # 3. Handle US/Canada 11-digit numbers that start with country code '1'
    if len(digits_only) == 11 and digits_only.startswith('1'):
        digits_only = digits_only[1:]

    # 4. Format the number if it's a standard 10-digit North American number
    if len(digits_only) == 10:
        formatted = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        # If it's not 10 digits, just return the raw digits (could be international)
        formatted = digits_only

    # 5. Append extension if one was found
    if extension:
        formatted += f" ext. {extension}"

    return formatted

# --- Test Cases ---
messy_numbers = [
    "+1 (555) 123-4567",
    "555.123.4567 ext 89",
    "1-800-555-0199 x42",
    "   5551234567   ",
    "44 20 7946 0958" # UK number (won't format as NA, just strips to digits)
]

for num in messy_numbers:
    print(f"Original: {num:<25} -> Cleaned: {clean_phone_number(num)}")
```

### Approach 2: The Production-Ready Way (Global)
If you are building an app that handles **international** numbers, you should never write your own regex. Phone number lengths and rules change by country. Instead, use the Python port of Google's `libphonenumber`.

*Note: You will need to install it first via terminal: `pip install phonenumbers`*

```python
import phonenumbers

def clean_and_validate_phone(phone_str, default_region="US"):
    """
    Cleans, validates, and formats a phone number to the E.164 international standard.
    E.164 format looks like: +15551234567
    """
    if not phone_str:
        return None

    try:
        # Parse the number (default_region helps if the number lacks a country code)
        parsed_number = phonenumbers.parse(phone_str, default_region)
        
        # Check if it's a mathematically valid number for its region
        if phonenumbers.is_valid_number(parsed_number):
            # Format to standard international E.164 (best for database storage)
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            return "Invalid Number"
            
    except phonenumbers.NumberParseException:
        return "Could not parse number"

# --- Test Cases ---
global_numbers = [
    ("(555) 123-4567", "US"),
    ("020 7946 0958", "GB"), # UK number without country code
    "+33 1 42 68 53 00",    # France
    "1-800-FLOWERS",        # Letters (libphonenumber handles keypad mapping)
]

for num, region in global_numbers:
    print(f"Original: {num:<20} -> Cleaned: {clean_and_validate_phone(num, region)}")
```

### Which should you use?
* Use **Approach 1** if you are doing quick data cleanup, scraping, or only care about US/Canada numbers and want to keep your code dependency-free.
* Use **Approach 2** if you are saving these numbers to a database, sending SMS messages, or dealing with users from multiple countries. Storing them in the **E.164 format** (`+15551234567`) is the gold standard for backend development.