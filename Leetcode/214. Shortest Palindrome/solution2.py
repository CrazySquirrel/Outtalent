class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        i = 0
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]: i += 1

        if i == n: return s

        return s[i:n][::-1] + self.shortestPalindrome(s[:i]) + s[i:]
