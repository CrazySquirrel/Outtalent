# Check by symbol

## Algorithm

* Iterate i from 0 to length of haystack minus length of needle:
    * If haystack[i] = needle[0] iterate j from 0 to length of needle while haystack[i + j] == needle[j]
    * If j equal to length of needle then return i
* Return -1

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i + j] == needle[j]: j += 1
                if j == len(needle): return i
        return -1
```

## Complexity Analysis:

* Time complexity: O(m * n)

* Space Complexity: O(1)

[Next](solution2.md)