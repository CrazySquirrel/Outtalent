class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = [0]

        def backtracking(s: str, t: str):
            if len(s) < len(t): return False
            if len(t) == 0:
                result[0] += 1
            else:
                for i in range(len(s)):
                    if t[0] == s[i]:
                        backtracking(s[i + 1:], t[1:])

        backtracking(s, t)

        return result[0]
