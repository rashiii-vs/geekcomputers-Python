# R25-T042 — click() Boundary Table

Source: Polyline.py

| Category | Initial state | Input | Expected behavior | Source contract |
|---|---|---|---|---|
| Valid boundary | polyline = [] | (0, 0) | Append the first point; result is [(0, 0)] | Line 5 initializes the empty list; line 10 appends the input |
| Valid interior | polyline = [(10, 20)] | (100, 50) | Preserve the existing point and append the new point | Line 10 appends the input |
| Unsupported values | Not specified | Not specified | No rejection rule or exception is defined by click() | Lines 8–10 |

## Public behavior

- Input: one argument, pos.
- Return: None (implicit).
- Mutation: appends pos to the global polyline list.
- GUI dependency: simplegui is used by the module and mocked in tests.

No unsupported-input rejection policy is invented.
