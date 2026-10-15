
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





