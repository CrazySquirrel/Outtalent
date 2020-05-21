class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1: return s

        result = []
        c, l = 2 * n - 2, len(s)

        for i in range(n):
            for j in range(0, l - i, c):
                result.append(s[j + i])
                if i != 0 and i != n - 1 and j + c - i < l:
                    result.append(s[j + c - i])

        return ''.join(result)
