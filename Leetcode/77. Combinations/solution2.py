class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(l: int, r: int, k: int, prefix: List[int]):
            if k == 0:
                result.append(prefix)
            else:
                for i in range(l, r):
                    dfs(i + 1, r, k - 1, prefix + [i])

        dfs(1, n + 1, k, [])

        return result
