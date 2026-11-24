# Contract Evidence — Project Euler Problem 10

## Source
File: solution to euler project problem 10.py

## Preconditions
- Input must be a positive integer.
- Source lines 8 and 16–19 document the positive-number restriction.
- Source line 15 documents the intended solution function.
## Case 1: Smallest valid input
- Input: 1
- Expected output: 0
- Actual output: 0
- Reason: There are no prime numbers below 1.
- Source reference: Lines 8 and 16–19.

## Case 2: Ordinary input
- Input: 10
- Expected output: 17
- Actual output: 17
- Reason: 2 + 3 + 5 + 7 = 17.
- Source reference: Line 5.

## Case 3: Prime boundary
- Input: 2
- Expected output: 0
- Actual output: 0
- Reason: The function sums primes strictly below 2, not including 2.
- Source reference: Lines 16–19.

## Additional verification
- Input: 1000
- Expected output: 76127
- Actual output: 76127
- Input: 2000000
- Expected output: 142913828922
- Actual output: 142913828922

## Observable mutation
- The function accepts an integer, not a mutable input object.
- The sieve list is created locally inside the function.
- No caller-visible mutation is specified.
- Mutation test: Not applicable to the documented interface.

## External dependencies and I/O
- The function uses Python built-ins only.
- No external packages or external I/O are required by the function.
- The original main block remains commented out.

## Baseline finding
- Before implementation, the target module imported successfully.
- No active solution() function was available.
- The baseline tests failed with AttributeError.
- Expected outputs were independently established before implementation.
