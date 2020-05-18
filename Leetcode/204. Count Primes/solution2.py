class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:  return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        for i in range(5, int(sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0: return False
        return True

    def countPrimes(self, n: int) -> int:
        counter = 0

        for i in range(2, n):
            if self.isPrime(i):
                counter += 1

        return counter
