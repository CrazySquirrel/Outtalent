from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t): return 0

        indexes = defaultdict(list)

        dp = [0] * (len(t) + 1)
        for i, c in enumerate(t): indexes[c].append(i + 1)

        for c in s:
            for i in indexes[c][::-1]: dp[i] += dp[i - 1]

            if c == t[0]: dp[1] += 1

        return dp[-1]
