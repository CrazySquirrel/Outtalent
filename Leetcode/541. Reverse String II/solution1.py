class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)

        result = []

        for i in range(0, N, k):
            if (i // k) % 2 == 0:
                result.append(s[i:min(i + k, N)][::-1])
            else:
                result.append(s[i:min(i + k, N)])

        return ''.join(result)
