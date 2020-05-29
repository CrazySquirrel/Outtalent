# Wrong solution

In a wrong way solution we can search for int by using regexp, then convert it to int and check for overflow since python supports big numbers. We can also limit the length of int in regexp.

```python
import re

INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31


class Solution:
    def myAtoi(self, str: str) -> int:
        x = re.search("^\s*([+-]?[0-9]+)", str)
        if not x: return 0
        x = int(x.group(1))
        if x < INT_MIN: return INT_MIN
        if INT_MAX < x: return INT_MAX
        return x
```

## Complexity Analysis

* Time Complexity: O((T+P)*2<sup>T+&#189;P</sup>) -> O(TP) <sup>*</sup>

* Space Complexity: O((T+P)*2<sup>T+&#189;P</sup>) -> O(TP) <sup>*</sup>

<sup>*</sup> - It's difficult to say because of the complexity of regular expression analysis, but if we take the analysis from [10. Regular Expression Matching](../10.%20Regular%20Expression%20Matching/README.md) as a basis, we'll get values above. In any case, this solution is not quite correct.

[Next](solution2.md)