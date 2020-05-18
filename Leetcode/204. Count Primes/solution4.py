import numpy as np


class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = np.ones((n,), dtype=np.bool)
        for i in range(2, int(n ** 0.5 + 1)):
            if isPrime[i]: isPrime[i * i:n:i] = False
        return max(np.sum(isPrime) - 2, 0)
