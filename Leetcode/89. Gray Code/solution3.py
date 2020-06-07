class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        if n == 2: return [0, 1, 3, 2]
        total = 2 ** n
        ret = [0] * total
        for i in range(total): ret[i] = i ^ (i >> 1)
        return ret
