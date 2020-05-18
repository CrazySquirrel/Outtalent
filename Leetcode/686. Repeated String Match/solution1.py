class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1, int(max(len(B) / len(A), 2) * 2)):
            if B in (A * i):
                return i
        return -1
