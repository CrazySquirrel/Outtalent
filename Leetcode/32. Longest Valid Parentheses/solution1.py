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
