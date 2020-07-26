class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [[inf] * len(key) for _ in ring]

        for i in range(len(ring)):
            if ring[i] == key[0]:
                dp[i][0] = min(i, len(ring) - i) + 1

        for j in range(1, len(key)):
            for i in range(len(ring)):
                if key[j] == ring[i]:
                    for k in range(len(ring)):
                        if ring[k] == key[j - 1]:
                            diff = abs(k - i)
                            dp[i][j] = min(dp[i][j], dp[k][j - 1] + min(diff, len(ring) - diff) + 1)

        res = inf

        for i in range(len(ring)):
            if ring[i] == key[-1]:
                for j in range(len(dp[i])):
                    res = min(res, dp[i][-1])

        return res
