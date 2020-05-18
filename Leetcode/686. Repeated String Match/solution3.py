import math


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if not set(B).issubset(set(A)): return -1

        base = math.ceil(len(B) / len(A))

        if B in A * (base + 1):
            return base if B in A * base else base + 1

        return -1
