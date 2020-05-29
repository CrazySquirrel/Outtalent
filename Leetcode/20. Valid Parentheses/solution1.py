class Solution:
    def isValid(self, s: str) -> bool:
        left_to_right = {'[': ']', '(': ')', '{': '}'}
        stack = []
        for c in s:
            if c in left_to_right:
                stack.append(left_to_right[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0
