class Solution:
    def findNthDigit(self, n: int) -> int:
        cnt, digits, cum = 9, 1, 1

        while n > cnt * digits:
            n -= cnt * digits
            cum += cnt
            cnt *= 10
            digits += 1

        number = (n - 1) // digits + cum
        offset = (n - 1) % digits

        return int(str(number)[offset])
