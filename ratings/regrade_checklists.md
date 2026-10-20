


# Re-grade checklists (blind, A and B swapped)

## amb-01: "Write a function that cleans up phone numbers."

### A
[ ] Notices the prompt is ambiguous ("clean up" could mean strip, format or validate): never mentions that the request is ambiguous
[~] Asks a clarifying question, or states its assumptions clearly (which country, what output): asks no question; gives some assumptions
[x] If it writes code: the code works for its stated assumptions: code works for what it assumes
[ ] Handles bad input sensibly ("abc", too short) instead of crashing or returning garbage: "abc" silently returns None, with no warning
[ ] Says what the function returns (digits only, or a formatted string): never says what the function returns

### B
[x] Notices the prompt is ambiguous ("clean up" could mean strip, format or validate): points out that "clean up" can mean different things
[x] Asks a clarifying question, or states its assumptions clearly (which country, what output): states its assumptions clearly
[x] If it writes code: the code works for its stated assumptions: code works for what it assumes
[x] Handles bad input sensibly ("abc", too short) instead of crashing or returning garbage: bad input is handled instead of slipping through
[x] Says what the function returns (digits only, or a formatted string): says clearly what it returns

---

## fix-01: average() crashes on an empty list

### A
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): identifies division by len(nums) when the list is empty
[x] Explains accurately why it crashes: explains the ZeroDivisionError correctly
[x] Gives the fixed function: provides a working fix
[x] Returns None for an empty list: empty list returns None
[x] Keeps the function name and signature: average(nums) unchanged
[x] Adds no new bug: no new problems introduced
[x] Stays concise: no padding, no tangents: to the point

### B
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): identifies division by len(nums) when the list is empty
[x] Explains accurately why it crashes: explains the ZeroDivisionError correctly
[x] Gives the fixed function: provides a working fix
[x] Returns None for an empty list: empty list returns None
[x] Keeps the function name and signature: average(nums) unchanged
[x] Adds no new bug: no new problems introduced
[x] Stays concise: no padding, no tangents: adds a few print examples, which are harmless

---

## impl-01: chunk(items, size)

### A
Hidden tests: pass 6/6
[x] Exact name and signature: chunk(items, size), as asked
[x] Consecutive chunks of length size: splits in order into chunks of size
[x] Last chunk may be shorter: short final chunk handled
[x] Raises ValueError when size < 1 (0 and negatives), and size 1 still works: raises for sizes below 1 only
[x] Matches the example: matches the example
[x] Handles edge cases (empty list, size bigger than the list): covered by the passing tests
[x] Clean, idiomatic code: clean and readable
[x] Stays concise: no padding, no tangents: to the point

### B
Hidden tests: pass 6/6
[x] Exact name and signature: chunk(items, size), as asked
[x] Consecutive chunks of length size: splits in order into chunks of size
[x] Last chunk may be shorter: short final chunk handled
[x] Raises ValueError when size < 1 (0 and negatives), and size 1 still works: raises for sizes below 1 only
[x] Matches the example: matches the example
[x] Handles edge cases (empty list, size bigger than the list): covered by the passing tests
[x] Clean, idiomatic code: clean and readable
[ ] Stays concise: no padding, no tangents: padded, with tangents beyond the task

---

## impl-03: is_anagram(a, b)

### A
Hidden tests: pass 4/4
[x] Exact name and signature, returns a bool: returns True or False
[x] Ignores case: case is ignored
[x] Ignores spaces (inside the string too, not just the ends): all spaces removed, not just the ends
[x] Compares letter counts correctly ("aab" vs "abb" is False): counts compared, not just letter sets
[x] Matches the example: "Dormitory" and "dirty room" give True
[x] Ignores nothing extra that wasn't asked for: only case and spaces ignored
[x] Clean, idiomatic code: clean and readable
[x] Stays concise: no padding, no tangents: to the point

### B
Hidden tests: pass 4/4
[x] Exact name and signature, returns a bool: returns True or False
[x] Ignores case: case is ignored
[x] Ignores spaces (inside the string too, not just the ends): all spaces removed, not just the ends
[x] Compares letter counts correctly ("aab" vs "abb" is False): counts compared, not just letter sets
[x] Matches the example: "Dormitory" and "dirty room" give True
[x] Ignores nothing extra that wasn't asked for: only case and spaces ignored
[x] Clean, idiomatic code: clean and readable
[x] Stays concise: no padding, no tangents: to the point

---

## ref-02: csv_line(values)

### A
Hidden tests: pass 4/4
[x] Keeps the name and signature: csv_line(values) unchanged
[x] Same output for every input (empty, single, mixed types, tuples): identical strings in every tested case
[x] Adds no new behavior (no quoting, no line ending): no csv module, no added quoting or newline
[x] More Pythonic (join, no index loop): uses join instead of the index loop
[x] More efficient, and explains why accurately: explains why join beats repeated concatenation
[x] Clean, idiomatic code: clean and readable
[x] Stays concise: no padding, no tangents: to the point

### B
Hidden tests: pass 4/4
[x] Keeps the name and signature: csv_line(values) unchanged
[x] Same output for every input (empty, single, mixed types, tuples): identical strings in every tested case
[x] Adds no new behavior (no quoting, no line ending): no csv module, no added quoting or newline
[x] More Pythonic (join, no index loop): uses join instead of the index loop
[x] More efficient, and explains why accurately: explains why join beats repeated concatenation
[x] Clean, idiomatic code: clean and readable
[x] Stays concise: no padding, no tangents: to the point
