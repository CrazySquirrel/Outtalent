class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = [int(d) for d in str(n)]

        return reduce(lambda x, y: x * y, l) - sum(l)
