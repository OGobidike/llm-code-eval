```python
def longest_unique_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        char_index_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

### Explanation
I use a sliding window approach with two pointers (`left` and `right`) to traverse the string while maintaining a dictionary that records the most recent index of each character. If we encounter a character already present within our current window, we shift the `left` pointer just past its previous occurrence to ensure the substring remains unique. This allows us to evaluate and track the maximum window size in a single $O(n)$ pass without needing to re-evaluate previously seen characters.