@lru_cache(None)
def binomial(n: int, k: int) -> int:
    if k == 0: return 1
    return binomial(n - 1, k - 1) * n // k


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        return self.fast_count(R + 1) - self.fast_count(L)

    def fast_count(self, N: int) -> int:
        S = bin(N)
        B = [len(S) + ~i for i, b in enumerate(S) if b == '1']
        res = 0
        for p in [2, 3, 5, 7, 11, 13, 17, 19]:
            if B[0] < p: break
            for i in range(min(p + 1, len(B))):
                n = B[i]
                k = p - i
                if n < k: break
                res += binomial(n, k)
        return res
