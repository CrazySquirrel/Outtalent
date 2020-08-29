class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if k > len(s): return -1
        if k == len(s): return 0

        @lru_cache(None)
        def toPalindrom(s: str) -> int:
            s = list(s)
            n = len(s)
            result = 0
            for i in range(n // 2):
                if s[i] == s[n - i - 1]: continue
                if s[i] < s[n - i - 1]:
                    s[n - i - 1] = s[i]
                else:
                    s[i] = s[n - i - 1]
                result += 1
            return result

        @lru_cache(None)
        def splitIntoChunks(s: str, k: int) -> int:
            if k <= 0: return 0
            if k == 1: return toPalindrom(s)
            return min([toPalindrom(s[:i]) + splitIntoChunks(s[i:], k - 1) for i in range(1, len(s) - k + 2)])

        return splitIntoChunks(s, k)
