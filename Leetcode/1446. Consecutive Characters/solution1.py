class Solution:
    def maxPower(self, s: str) -> int:
        result = counter = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                result = max(result, counter)
                counter = 0
            counter += 1
        return max(result, counter)
