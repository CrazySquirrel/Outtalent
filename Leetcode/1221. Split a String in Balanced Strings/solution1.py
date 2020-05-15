class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        counter = 0

        for c in s:
            if c == 'R':
                counter += 1
            else:
                counter -= 1

            if counter == 0:
                result += 1

        return result
