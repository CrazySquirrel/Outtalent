class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def collect(y: int, r1x: int, r2x: int) -> int:
            if y >= m: return 0
            res = 0
            for x1 in (-1, 0, 1):
                if not (0 <= r1x + x1 < n): continue
                for x2 in (-1, 0, 1):
                    if not (0 <= r2x + x2 < n): continue
                    res = max(res, collect(y + 1, r1x + x1, r2x + x2))
            return res + (grid[y][r1x] + grid[y][r2x] if r1x != r2x else grid[y][r1x])

        return collect(0, 0, n - 1)
