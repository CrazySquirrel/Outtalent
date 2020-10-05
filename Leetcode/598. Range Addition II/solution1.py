class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for om, on in ops: m, n = min(m, om), min(n, on)
        return m * n
