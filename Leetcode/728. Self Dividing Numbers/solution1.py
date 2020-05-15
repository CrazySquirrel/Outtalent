class Solution:
    def isSelfDivided(self, n: int) -> bool:
        m = n

        while n:
            if n % 10 == 0 or m % (n % 10) != 0: return False
            n //= 10

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return list(filter(self.isSelfDivided, range(left, right + 1)))
