class Solution:
    def allUnique(self, s: str, start: int, end: int) -> bool:
        h = set()

        for i in range(start, end):
            if s[i] in h: return False
            h.add(s[i])

        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.allUnique(s, i, j):
                    ans = max(ans, j - i)

        return ans
