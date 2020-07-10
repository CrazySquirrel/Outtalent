class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = len(nums)

        sums = [n for n in nums]

        for i in range(1, l): sums[i] += sums[i - 1]

        @lru_cache(None)
        def get_sum(i: int, j: int) -> int:
            if i == 0: return sums[j]
            return sums[j] - sums[i - 1]

        @lru_cache(None)
        def dfs(i: int, k: int) -> int:
            if k == 1: return get_sum(i, l - 1)
            result = inf
            for j in range(i, l - k + 1):
                result = min(result, max(get_sum(i, j), dfs(j + 1, k - 1)))
            return result

        return dfs(0, m)
