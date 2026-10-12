python
```
def longest_unique_substring(s: str) -> int:
    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

Approach: Use a sliding window defined by `left` and `right` to track a substring with no repeated characters, and a dictionary to store each character's most recent index. When a repeated character appears inside the current window, move `left` just past its previous occurrence, then update the maximum window length.

Time complexity: $O(n)$, because each character is processed once. Space complexity: $O(k)$, where $k$ is the number of distinct characters encountered.

Example: `longest_unique_substring("abcabcbb")` returns `3`, corresponding to `"abc"`.