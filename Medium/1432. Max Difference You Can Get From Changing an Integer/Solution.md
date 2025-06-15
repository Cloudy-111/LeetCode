# Solution: Maximum Difference by Digit Replacement

## Problem Summary:

Given an integer num, you need to:

- Apply one digit replacement operation twice independently:

- Choose a digit x (0–9),

- Replace all occurrences of x in num with another digit y (0–9, y can be the same as x),

The result must not have leading zeros or become zero.

Let a and b be the two results after performing two different replacements on num.

Return max(a - b) — the maximum difference between any two possible outcomes of the above operation.

## Key Observations:

- To maximize the result, we want to increase digits — ideally replacing some digit x with 9.
- To minimize the result, we want to decrease digits — ideally replacing some digit x with 1 or 0, depending on the position.

### But we must not allow leading zeros — so the first digit of the result must never become 0.

## Strategy Overview:

### Maximize:

- Find the first digit in num that is not 9.
- Replace all occurrences of that digit with 9.

### Minimize:

- If first digit is not 1, replace it with 1 (to avoid leading 0).
- If first digit is 1, look for any other digit (not 0 or 1) and replace it with 0.
