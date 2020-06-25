# Brute Force

## Algorithm

* If there is no s then return 0
* If string is valid parentheses then return length of s
* Return max of longestValidParentheses(s[1:]) and longestValidParentheses(s[:-1])

```python
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'[': ']', '(': ')', '{': '}'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(dic[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0

    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        if self.isValid(s): return len(s)
        return max(self.longestValidParentheses(s[1:]), self.longestValidParentheses(s[:-1]))
```

## Complexity Analysis

Time complexity: O(n<sup>3</sup>)

Space complexity: O(n)

[Next](solution2.md)