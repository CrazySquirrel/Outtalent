from collections import Counter, defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()): return []

        dp = defaultdict(list)
        dp[0] = [[]]

        wordDict = set(wordDict)

        for j in range(1, len(s) + 1):
            for i in range(j):
                sub = s[i:j]
                if sub in wordDict and i in dp:
                    dp[j].extend([pre + [sub] for pre in dp[i]])

        return [" ".join(phrase) for phrase in dp[len(s)]]
