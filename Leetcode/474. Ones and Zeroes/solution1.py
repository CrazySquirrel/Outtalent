class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i: int, m: int, n: int) -> int:
            if i >= len(strs): return 0
            one_num = strs[i].count('1')
            zero_num = len(strs[i]) - one_num
            max_form = dfs(i + 1, m, n)
            if zero_num <= m and one_num <= n:
                max_form = max(max_form, dfs(i + 1, m - zero_num, n - one_num) + 1)
            return max_form

        return dfs(0, m, n)
