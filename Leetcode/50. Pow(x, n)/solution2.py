class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x

        temp = self.myPow(x, int(n / 2))

        if n % 2 == 0: return temp * temp
        if n > 0: return x * temp * temp

        return (temp * temp) / x
