
# 1: amb-01 (ambiguous, graded by reading)

Write a function that cleans up phone numbers.

## Quick checklist for  amb -01
- What does “clean up” mean? Remove spaces and dashes? Reformat? Validate?
- Which country’s numbers? A Nigerian number and a US number look different.
- What should happen with a bad input, like "abc" or a number that’s too short?
- What should the function return: digits only, or a formatted string?

## amb-01: "Write a function that cleans up phone numbers."

What would be a perfect answer:

Response A

[x] Notices the prompt is ambiguous ("clean up" could mean strip, format or validate) : Addresses ambiguity of prompt directly. Says that "cleaning up a phone number can mean many different things"

[x] Either asks a clarifying question, or states its assumptions clearly (which country, what output): No clarifying question, but states it's assumptions

[x] If it writes code: The code works for its stated assumptions

[~] Handles bad input sensibly ("abc", too short) instead of crashing or returning garbanzo beanz: handles edges cases in the If statement, but edge cases where there are only letters get silently returned. But it does handle others like "".

[x] Says what the function returns (digits only, or a formatted string): Formats into 10-digit US/Canada numbers

Response B

[ ] Notices the prompt is ambiguous ("clean up" could mean strip, format or validate): "Never asks clarifing steps"

[x] Either asks a clarifying question, or states its assumptions clearly (which country, what output): it does ste it's assumptions clearly 

[x] If it writes code: The code works for its stated assumptions

[ ] Handles bad input sensibly ("abc", too short) instead of crashing or returning garbanzo beanz: "bad inputs silently give garbage, "abc" returns none with no warning."

[ ] Says what the function returns (digits only, or a formatted string): says what it does, not what it returns

---
# 2. exp-01

## exp-01

Requirements from the prompt:
- Explains why `result` is `None` (what `.sort()` does to the list, and what it returns)
- Names what to use instead to get a sorted list back
- Says when to choose each option: `.sort()` and the alternative, both of them

### A
[x] Explains the why behind the result being None: explains that `.sort()` sorts the list in place and returns None
[x] Names what to use to get a sorted list back: names `sorted()` explicitly
[x] Says when to choose each (both): `.sort()` to modify the existing list; `sorted()` to create a new one
[x] Gets every technical claim right: uses `.sort()` and `sorted()` correctly throughout
[x] Shows a correct, minimal example where it helps: shows `sorted()` returning a new list, including in reverse order
[x] Gives the practical takeaway: explains where each option fits in practice
[ ] Stays concise: no padding, no tangents: too wordy for a short question

### B
[x] Explains the why behind the result being None: explains the cause clearly
[x] Names what to use to get a sorted list back: explains and demonstrates both options
[x] Says when to choose each (both): states when to use each option
[x] Gets every technical claim right: all claims are accurate
[x] Shows a correct, minimal example where it helps: includes a correct example
[x] Gives the practical takeaway: ends with a clear takeaway
[~] Stays concise: no padding, no tangents: only slightly long

---

# 3. exp-02

## exp-02

Requirements from the prompt:
- States the time complexity of `common(a, b)` in Big-O, with its variables named (what n and m stand for)
- Explains why: walks through what each line of the function costs
- Answers whether it could be faster, and shows or describes how

### A
[x] States the complexity, with variables named: states O(n^2) and explains why
[x] Explains why, line by line: breaks down the cost of each line
[x] Says whether and how it could be faster: explains how, with an example that uses a second set doesnt walk through line by line
[x] Gets every technical claim right: no mis-statements about how the operations behave
[x] Shows a correct, minimal example where it helps: shows that tracking seen output items in a set or dict lowers the complexity
[ ] Gives the practical takeaway: doesn't explain why the faster version works
[~] Stays concise: no padding, no tangents: no unnecessary additions

### B
[x] States the complexity, with variables named: names n and m and gives O(n^2), or O(n + m^2)
[x] Explains why, line by line: explains that rechecking `out` inside the loop causes the jump in complexity
[x] Says whether and how it could be faster: explains how, with examples using dictionaries
[x] Gets every technical claim right: all claims are accurate
[x] Shows a correct, minimal example where it helps: shows code that brings the time down to O(n)
[x] Gives the practical takeaway: ends with a thorough explanation
[x] Stays concise: no padding, no tangents: longer than A, but no padding or tangents

---

# 4. exp-03

## exp-03

Requirements from the prompt:
- Explains the difference between `is` and `==` (what each one compares)
- Gives an example where `is` and `==` disagree
- Says when `is` is the right choice

### A
[x] Explains the difference (what each compares): explains that `is` checks identity (the same object) and `==` checks equality of contents
[x] Gives an example where they disagree: a clear example where `a == b` is True but `a is b` is False
[x] Says when `is` is the right choice: stated clearly
[x] Gets every technical claim right: no errors found
[x] Shows a correct, minimal example where it helps: shows when to use each operator
[x] Gives the practical takeaway: explains the reasoning behind each use
[ ] Stays concise: no padding, no tangents: very wordy

### B
[x] Explains the difference (what each compares): explains that `is` checks identity (the same object) and `==` checks equality of contents
[x] Gives an example where they disagree: a clear example where `a == b` is True but `a is b` is False, with the True/False output shown
[x] Says when `is` is the right choice: stated clearly
[x] Gets every technical claim right: no errors found
[x] Shows a correct, minimal example where it helps: shows when to use each operator
[x] Gives the practical takeaway: explains the reasoning behind each use
[ ] Stays concise: no padding, no tangents: very wordy

---

# 5. fix-01

## fix-01

Requirements from the prompt:
- Finds the bug: the cause, not just "it crashes"
- Explains why it crashes
- Gives the fixed function: returns the average, and None for an empty list

### A
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): identifies that len(nums) is 0 for an empty list, causing a ZeroDivisionError
[x] Explains accurately why it crashes: explains that an `if not nums` check is needed before dividing
[x] Gives the fixed function: provides a working fix
[x] Returns None for an empty list:
[x] Keeps the function name and signature:
[x] Adds no new bug:
[x] Stays concise: no padding, no tangents: stays on task

### B
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): identifies that len(nums) is 0 for an empty list, causing a ZeroDivisionError
[x] Explains accurately why it crashes: explains that an `if not nums` check is needed before dividing
[x] Gives the fixed function: provides a working fix
[x] Returns None for an empty list:
[x] Keeps the function name and signature:
[x] Adds no new bug:
[x] Stays concise: no padding, no tangents: stays on task

---

# 6. fix-02

## fix-02

Requirements from the prompt:
- Explains why the second call still contains the first call's tag
- Fixes `add_tag` so each call without `tags` starts from an empty list

### A
Hidden tests: pass 2/2
[x] Finds the real bug (the cause, not the symptom): identifies that the default argument is evaluated only once, when the function is defined
[x] Explains accurately why it happens: explains that every call without `tags` reuses the same list, so earlier tags persist
[x] Gives the fixed function: uses `tags=None` as the default and creates a new list inside when `tags is None`
[x] Each call without `tags` starts empty: a new list is created on each such call
[x] Keeps the function name and signature: yes
[x] Adds no new bug: checks `is None`, so a caller's own empty list is still used
[x] Stays concise: no padding, no tangents: very concise and easy to follow

### B
Hidden tests: pass 2/2
[x] Finds the real bug (the cause, not the symptom): identifies that the default argument is evaluated only once, when the function is defined
[x] Explains accurately why it happens: explains that every call without `tags` reuses the same list, so earlier tags persist
[x] Gives the fixed function: uses `tags=None` as the default and creates a new list inside when `tags is None`
[x] Each call without `tags` starts empty: a new list is created on each such call
[x] Keeps the function name and signature: yes
[x] Adds no new bug: checks `is None`, so a caller's own empty list is still used
[x] Stays concise: no padding, no tangents: very concise and easy to follow

---

# 7. fix-03

## fix-03

Requirements from the prompt:
- Explains why the search sometimes never finishes
- Gives a fixed `binary_search(nums, target)` that returns the index of `target`, or -1 if it's missing

### A
Hidden tests: pass 7/7
[x] Finds the real bug (the cause, not the symptom): identifies that `lo = mid` / `hi = mid` never move past mid, so the search range can stop shrinking
[x] Explains accurately why it loops forever: explains that once the range stops shrinking, the same mid is checked again on every loop
[x] Gives the fixed function: uses `mid + 1` / `mid - 1`
[x] Returns -1 when the target is missing:
[x] Keeps the function name and signature:
[x] Adds no new bug:
[x] Stays concise: no padding, no tangents: concise

### B
Hidden tests: pass 7/7
[x] Finds the real bug (the cause, not the symptom): identifies that `lo = mid` / `hi = mid` never move past mid, so the search range can stop shrinking
[x] Explains accurately why it loops forever: explains that once the range stops shrinking, the same mid is checked again on every loop
[x] Gives the fixed function: uses `mid + 1` / `mid - 1`, with helpful comments explaining each fix
[x] Returns -1 when the target is missing:
[x] Keeps the function name and signature:
[x] Adds no new bug:
[x] Stays concise: no padding, no tangents: concise

---

# 8. fix-04

## fix-04

Requirements from the prompt:
- Explains why the loop raises "dictionary changed size during iteration"
- Fixes `remove_low_stock` so it removes every item below `minimum`
- Returns the same dict (the caller's object), not a new one

### A
Hidden tests: fail 2/3 (test_returns_same_dict)
[x] Finds the real bug (the cause, not the symptom): identifies deleting from the dict while looping over it
[x] Explains accurately why it raises the error: explains that removing items while iterating changes the dict's size
[x] Removes every item below minimum: main fix loops over list(stock.keys()) and deletes with <
[~] Returns the same dict, not a new one: main fix does, but the final alternative builds and returns a new dict
[x] Keeps the function name and signature: yes
[ ] Adds no new bug: the alternative returns a new dict, so the caller's dict is left unchanged
[x] Stays concise: no padding, no tangents:

### B
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): yes
[x] Explains accurately why it raises the error: clear explanation of why deleting during iteration raises the RuntimeError
[x] Removes every item below minimum: loops over list(stock) and deletes with <
[x] Returns the same dict, not a new one: modifies stock in place and says so clearly
[x] Keeps the function name and signature: yes
[x] Adds no new bug: correct
[x] Stays concise: no padding, no tangents: includes worked examples

---

# 9. fix-05

## fix-05

Requirements from the prompt:
- Explains why `list(set(items))` gets the order wrong
- Fixes `dedupe` so it removes duplicates
- Keeps the first occurrence of each item, in original order

### A
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): identifies that sets are unordered
[x] Explains accurately why the order is wrong: explains that Python sets don't keep insertion order
[x] Removes duplicates: uses list(dict.fromkeys(items)), with a seen-set loop as an alternative; both O(n)
[x] Keeps first occurrences in original order: the first occurrence of each item is kept, in order
[x] Keeps the function name and signature: yes
[x] Adds no new bug: none found; dict.fromkeys keeps each item once as a key, in insertion order
[x] Stays concise: no padding, no tangents: clear and concise

### B
Hidden tests: pass 3/3
[x] Finds the real bug (the cause, not the symptom): identifies that sets are unordered
[x] Explains accurately why the order is wrong: explains that Python sets don't keep insertion order
[x] Removes duplicates: uses list(dict.fromkeys(items)), with a seen-set loop as an alternative; both O(n)
[x] Keeps first occurrences in original order: the first occurrence of each item is kept, in order
[x] Keeps the function name and signature: yes
[x] Adds no new bug: none found; dict.fromkeys keeps each item once as a key, in insertion order
[x] Stays concise: no padding, no tangents: clearer and more concise than A; easier to read

---
