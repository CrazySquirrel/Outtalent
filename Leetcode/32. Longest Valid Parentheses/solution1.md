# Brute Force

## Algorithm

* If there is no s then return 0
* If string is valid parentheses then return length of s
* Return max of longestValidParentheses(s[1:]) and longestValidParentheses(s[:-1])

```python
class Solution:
    def isValid(self, s: str) -> bool:
        counter = 0
        for c in s:
            counter += 1 if c == '(' else -1
            if counter == -1: return False
        return counter == 0

    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        if self.isValid(s): return len(s)
        return max(self.longestValidParentheses(s[1:]), self.longestValidParentheses(s[:-1]))
```

## Complexity Analysis

Time complexity: O(n<sup>3</sup>)

Space complexity: O(n<sup>2</sup>)

[Next](solution2.md)