class Solution:
    def rotatedDigits(self, N: int) -> int:
        bad = {3, 4, 7}
        good = {2, 5, 6, 9}
        result = 0
        for i in range(1, N + 1):
            is_good = False
            while i:
                if i % 10 in bad:
                    is_good = False
                    break
                if i % 10 in good:
                    is_good = True
                i //= 10
            if is_good:
                result += 1
        return result
