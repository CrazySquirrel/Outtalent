class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        length = start = 0

        for i, c in enumerate(S):
            if c.isdigit():
                length *= int(c)
            else:
                length += 1

            if length >= K:
                start = i
                break

        for i in range(start, -1, -1):
            if S[i].isdigit():
                length = length // int(S[i])
                K %= length
            else:
                if K == 0 or K == length: return S[i]
                length -= 1
