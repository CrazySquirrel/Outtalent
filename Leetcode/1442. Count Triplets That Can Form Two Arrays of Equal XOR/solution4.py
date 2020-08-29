class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = cur = 0
        count = {0: (1, 0)}
        for i, a in enumerate(arr):
            cur ^= a
            n, total = count.get(cur, (0, 0))
            count[cur] = (n + 1, total + i + 1)
            res += i * n - total
        return res
