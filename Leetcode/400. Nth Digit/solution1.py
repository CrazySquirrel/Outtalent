class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1 - 9       | 9
        # 10 - 99     | 90 * 2 -> 178
        # 100 - 999   | 900 * 3 -> 2697
        # 1000 - 9999 | 9000 * 4 -> 35996
        # n = 1000 -> 1000 - 9 - 90 * 2 -> (811 - 1)//3 + 100 -> 270 + 100 -> 370
        # (811 - 1) % 3 -> 0
        # 370[0] -> 3
        digits = base = 1
        while n > 9 * base * digits:
            n -= 9 * base * digits
            base *= 10
            digits += 1
        q, r = divmod(n - 1, digits)
        return int(str(base + q)[r])
