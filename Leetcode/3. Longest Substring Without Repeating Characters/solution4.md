# Sliding Window Optimized (ASCII 128)

The previous implements all have no assumption on the charset of the string s.

If we know that the charset is rather small, we can replace the Map with an integer array as direct access table.

Commonly used tables are:

* int[26] for Letters 'a' - 'z' or 'A' - 'Z'
* int[128] for ASCII
* int[256] for Extended ASCII

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = [0] * 128
        ans = i = 0
        for j in range(n):
            i = max(i, h[ord(s[j])])
            ans = max(ans, j - i + 1)
            h[ord(s[j])] = j + 1
        return ans
```

## Complexity Analysis

* Time complexity: O(n). 

Index j will iterate n times.

* Space complexity: O(m). 

m is the size of the charset (128).

[Prev](solution3.md) [Next](solution5.md)