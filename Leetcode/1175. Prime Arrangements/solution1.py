from math import factorial


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        for prime in range(2, int(n ** 0.5) + 1):
            if not primes[prime]: continue
            for composite in range(prime * prime, n + 1, prime): primes[composite] = False
        cnt = sum(primes[2:])
        return factorial(cnt) * factorial(n - cnt) % (10 ** 9 + 7)
