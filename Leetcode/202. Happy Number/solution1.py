class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
