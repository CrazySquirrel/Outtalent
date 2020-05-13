class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ, prod = 0, 1

        while n:
            summ += n % 10
            prod *= n % 10
            n = n // 10

        return prod - summ
