# Slices

## Algorithm

* Iterate i from 0 to length of haystack minus length of needle:
    * If haystack from i to i + length of needle equal to needle then return i
* Return -1

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
```

## Complexity Analysis:

* Time complexity: O(m * n)

* Space Complexity: O(n)

[Prev](solution1.md) [Next](solution3.md)