class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: return [0][K - 1]
        if N == 2: return [0, 1][K - 1]
        current = [1, 0] if self.kthGrammar(N - 1, (K + 1) // 2) else [0, 1]
        return current[0] if K % 2 == 1 else current[1]
