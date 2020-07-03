class Solution:
    ugly = sorted(2 ** a * 3 ** b * 5 ** c for a in range(32) for b in range(20) for c in range(14))

    def nthUglyNumber(self, n: int) -> int:
        return self.ugly[n - 1]
