class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        res = self.grayCode(n - 1)
        for i in range(len(res) - 1, -1, -1): res.append((2 ** (n - 1)) + res[i])
        return res
