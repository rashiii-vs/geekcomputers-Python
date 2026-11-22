# R25-T042 — Test Case Evidence

## Test 1: Smallest valid input

Source precondition:
Polyline.py line 5 initializes polyline as an empty list.

Literal initial state:
polyline = []

Literal input:
pos = (0, 0)

Independently calculated expected output:
polyline = [(0, 0)]
return = None

Actual output:
polyline = [(0, 0)]
return = None

Result: PASSED

## Test 2: Ordinary input

Source precondition:
Polyline.py line 5 initializes polyline as an empty list.
The test fixture then adds the existing point (10, 20).

Literal initial state:
polyline = [(10, 20)]

Literal input:
pos = (100, 50)

Independently calculated expected output:
polyline = [(10, 20), (100, 50)]
return = None

Actual output:
polyline = [(10, 20), (100, 50)]
return = None

Result: PASSED

## Summary

Total tests: 2
Passed: 2
Failed: 0
