class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dp = collections.defaultdict(dict)

        for (a, b), v in zip(equations, values):
            dp[a][a] = dp[b][b] = 1.0
            dp[a][b] = v
            dp[b][a] = 1 / v

        for i, j, v in itertools.permutations(dp.keys(), 3):
            if j in dp[i] and v in dp[j]:
                dp[i][v] = dp[i][j] * dp[j][v]

        return [dp[a][b] if a in dp and b in dp[a] else -1.0 for a, b in queries]
