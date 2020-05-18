class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        isPrime[:2] = [False, False]
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]: isPrime[i * i: n: i] = [False] * len(isPrime[i * i: n: i])
        return sum(isPrime)
