class Solution:
    def integerReplacement(self, n: int) -> int:
        result = 0

        while n > 1:
            result += 1

            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1

        return result
