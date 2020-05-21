class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'[': ']', '(': ')', '{': '}'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(dic[c])
            elif len(stack) == 0 or stack[-1] != c:
                return False
            else:
                stack.pop()
        return len(stack) == 0
