class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []

        for i in range(2, n):
            for prime in primes:
                if i % prime == 0: break
            else:
                primes.append(i)

        return len(primes)
