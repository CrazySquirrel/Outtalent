class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        result = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - c - 1):
                    result.append('({}){}'.format(left, right))
        return result
