class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])

        mins = [[] for _ in range(m)]

        for i in range(m):
            m1 = m2 = inf
            k1 = k2 = 0
            for j in range(n):
                if arr[i][j] < m1:
                    m2, m1 = m1, arr[i][j]
                    k2, k1 = k1, j
                elif arr[i][j] < m2:
                    m2 = arr[i][j]
                    k2 = j
            mins[i] = (m1, k1, m2, k2)

        @lru_cache(None)
        def count(i: int, j: int) -> int:
            if i >= m: return 0

            m1, k1, m2, k2 = mins[i]

            if k1 == j:
                return m2 + count(i + 1, k2)

            if k2 == j:
                return m1 + count(i + 1, k1)

            return min(m1 + count(i + 1, k1), m2 + count(i + 1, k2))

        return count(0, -1)
