class Solution:
    def helper(self, n: int) -> List[str]:
        if n == 0: return ['0']
        if n == 1: return ['0', '1']
        pre = self.helper(n - 1)
        return ['0' + c for c in pre] + ['1' + c for c in pre[::-1]]

    def grayCode(self, n: int) -> List[int]:
        return [int(x, 2) for x in self.helper(n)]
