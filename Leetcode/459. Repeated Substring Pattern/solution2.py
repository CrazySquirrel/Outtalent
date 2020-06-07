import numpy as np


class Solution:
    def getPrimes(self, n: int) -> List[int]:
        isPrime = np.ones((n,), dtype=np.bool)
        for i in range(2, int(n ** 0.5 + 1)):
            if isPrime[i]: isPrime[i * i:n:i] = False
        return [i for i, v in enumerate(isPrime) if v and i >= 2]

    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for p in self.getPrimes(l + 1):
            if l % p == 0 and s[:l // p] * p == s: return True
        return False
