# Dynamic Programming Top-Down

As the problem has an optimal substructure, it is natural to cache intermediate results. We ask the question dp(i, j): does text[i:] and pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

We proceed with the same recursion as in [Approach 1](./solution1.md), except because calls will only ever be made to match(text[i:], pattern[j:]), we use dp(i, j) to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.

```python
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if j == len(pattern): return i == len(text)
            
            first_match = i < len(text) and (pattern[j] == text[i] or pattern[j] == '.')
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                return dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)
```

## Complexity Analysis

* Time Complexity: O(TP).

* Space Complexity: O(TP).

[Prev](solution1.md) [Next](solution3.md)
