

Python
```
def is_anagram(a, b):
    return sorted(a.lower().replace(" ", "")) == sorted(b.lower().replace(" ", ""))

# Example usage
print(is_anagram("Dormitory", "dirty room"))  # True
print(is_anagram("listen", "silent"))         # True
print(is_anagram("hello", "world"))           # False
```

How it works:

1. `.lower()` converts both strings to lowercase, ignoring case.
2. `.replace(" ", "")` removes spaces.
3. `sorted()` sorts the characters alphabetically.
4. `==` compares the sorted characters. If they match, the strings are anagrams, so the function returns `True`; otherwise, it returns `False`.
