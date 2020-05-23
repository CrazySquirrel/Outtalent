class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        result = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result
