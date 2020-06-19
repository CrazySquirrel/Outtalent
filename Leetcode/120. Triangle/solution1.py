class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(l: int, i: int) -> int:
            if l >= len(triangle) or i >= len(triangle[l]): return 0
            return triangle[l][i] + min(dfs(l + 1, i), dfs(l + 1, i + 1))

        return dfs(0, 0)
