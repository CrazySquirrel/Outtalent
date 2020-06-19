class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path):
            if not s:
                res.append(path)
            else:
                for i in range(len(s)):
                    if isPal(s[:i + 1]): dfs(s[i + 1:], path + [s[:i + 1]])

        @lru_cache(None)
        def isPal(s):
            return s == s[::-1]

        res = []
        dfs(s, [])
        return res
