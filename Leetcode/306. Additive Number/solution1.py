class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isValid(n: str) -> bool:
            return len(n) == 1 or n[0] != '0'

        def helper(first: str, second: str, rest: str) -> bool:
            third = str(int(first) + int(second))

            if not isValid(third): return False

            if len(rest) < len(third): return False

            if third == rest: return True

            if third != rest[:len(third)]: return False

            return helper(second, third, rest[len(third):])

        for i in range(len(num) - 2):
            first = num[:i + 1]

            if not isValid(first): break

            for j in range(i + 1, len(num) - 1):
                second = num[(i + 1):(j + 1)]

                if not isValid(second): break

                if helper(first, second, num[(j + 1):]): return True

        return False
