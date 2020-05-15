class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        counter = 0
        for c in S:
            if c == '(':
                if counter > 0: result += c
                counter += 1
            elif c == ')':
                counter -= 1
                if counter > 0: result += c
        return ''.join(result)
