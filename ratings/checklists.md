
## amb-01 (ambiguous, graded by reading)

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



