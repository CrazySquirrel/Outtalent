# Reverse check

# Algorithm

1. Create roman to arabic dictionary

> {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

2. Go through string backwards and check:
    1. Update prev arabic and convert current roman number to new current arabic
    2. If prev arabic less than current then we increment result by current, otherwise we decrement

```python
ROMAN_TO_INT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        last = curr = result = 0
        for c in s[::-1]:
            last, curr = curr, ROMAN_TO_INT[c]
            result += curr if curr >= last else -curr
        return result
```

## Complexity Analysis

* Time complexity: O(n). 

* Space complexity: O(1).
