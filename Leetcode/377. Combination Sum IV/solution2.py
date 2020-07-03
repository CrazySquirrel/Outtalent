class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(t: int) -> int:
            if t < 0: return 0
            if t == 0: return 1
            return sum(dfs(t - n) for n in nums if n <= t)

        return dfs(target)
