class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        R, i = '', 0
        for s in S:
            if s.isdigit():
                R *= int(s)
            else:
                R += s
            if len(R) >= K: return R[K - 1]
        return R[K - 1]
