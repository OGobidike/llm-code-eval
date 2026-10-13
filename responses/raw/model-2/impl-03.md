Here is the Python function to check if two strings are anagrams. 

The simplest way to solve this is to remove the spaces, convert everything to lowercase, and then compare the sorted characters of both strings.

```python
def is_anagram(a, b):
    # Remove spaces and convert to lowercase
    clean_a = a.replace(" ", "").lower()
    clean_b = b.replace(" ", "").lower()
    
    # If the lengths don't match, they can't be anagrams
    if len(clean_a) != len(clean_b):
        return False
        
    # Compare the sorted characters of both strings
    return sorted(clean_a) == sorted(clean_b)

# Test the example
print(is_anagram("Dormitory", "dirty room"))  # Output: True
print(is_anagram("Hello", "Oleh"))            # Output: False
```

### Alternative (More Efficient for Long Strings)
If you are dealing with very long strings, sorting them takes **O(N log N)** time. You can achieve **O(N)** time complexity by using Python's built-in `collections.Counter`, which counts the occurrences of each character:

```python
from collections import Counter

def is_anagram_fast(a, b):
    clean_a = a.replace(" ", "").lower()
    clean_b = b.replace(" ", "").lower()
    
    return Counter(clean_a) == Counter(clean_b)
```
Both methods will perfectly handle your "Dormitory" / "dirty room" example!