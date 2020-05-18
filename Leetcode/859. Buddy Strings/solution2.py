class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B: return len(A) > len(set(A))
        pairs = []
        for a, b in zip(A, B):
            if a != b: pairs.append((a, b))
            if len(pairs) > 2: return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
