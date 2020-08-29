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
