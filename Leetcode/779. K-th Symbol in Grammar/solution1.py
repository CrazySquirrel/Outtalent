class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        a = [0]
        b = [0, 1]
        for i in range(1, N):
            a = b
            b = [0] * len(a) * 2
            for j in range(0, len(b), 2):
                if a[j // 2] == 0:
                    b[j + 1] = 1
                else:
                    b[j] = 1
        return a[K - 1]
