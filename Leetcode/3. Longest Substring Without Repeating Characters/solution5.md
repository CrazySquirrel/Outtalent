# Sliding Window Optimized

We going to use the same solution as for [Sliding Window Optimized (HashMap)](solution3.md) by with some coding optimizations.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        ans = j = 0
        for i, c in enumerate(s):
            if c in h: j = max(j, h[c] + 1)
            ans = max(ans, i - j + 1)
            h[c] = i
        return ans
```

[Prev](solution4.md)