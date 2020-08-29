class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])

        @lru_cache(None)
        def count(i: int, j: int) -> int:
            if i >= m: return 0
            result = inf
            for k in range(n):
                if j != k: result = min(result, arr[i][k] + count(i + 1, k))
            return result

        return count(0, -1)
