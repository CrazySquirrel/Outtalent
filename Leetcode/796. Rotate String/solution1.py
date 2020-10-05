class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B: return True
        return len(A) == len(B) and B in A + A
