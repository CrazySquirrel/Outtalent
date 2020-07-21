class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        result = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append('({}){}'.format(left, right))
        return result
