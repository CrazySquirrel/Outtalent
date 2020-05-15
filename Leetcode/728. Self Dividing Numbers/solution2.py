class Solution:
    cache = set()

    def isSelfDivided(self, n: int) -> bool:
        if n in Solution.cache: return n

        m = n

        while n:
            if n % 10 == 0 or m % (n % 10) != 0: return False
            n //= 10

        Solution.cache.add(m)

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return list(filter(self.isSelfDivided, range(left, right + 1)))
