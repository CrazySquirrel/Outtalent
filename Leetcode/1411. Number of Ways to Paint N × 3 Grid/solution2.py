class Solution:
    def numOfWays(self, n: int) -> int:
        p121, p123, m = 6, 6, 1e9 + 7
        for i in range(1, n):
            p121, p123 = (p121 * 3 + p123 * 2) % m, (p121 * 2 + p123 * 2) % m
        return int((p121 + p123) % m)
