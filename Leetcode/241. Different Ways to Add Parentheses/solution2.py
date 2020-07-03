class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        f = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        @lru_cache(None)
        def dfs(l: int, r: int):
            if l >= r: return []

            result = []

            for i in range(l, r):
                if input[i] not in f: continue

                lefts = dfs(l, i)
                rights = dfs(i + 1, r)

                for left in lefts:
                    for right in rights:
                        result.append(f[input[i]](left, right))

            return result if result else [int(input[l:r])]

        return dfs(0, len(input))
