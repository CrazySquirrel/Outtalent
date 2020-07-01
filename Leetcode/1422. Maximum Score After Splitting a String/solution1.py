class Solution:
    def maxScore(self, s: str) -> int:
        left = s[0].count('0')
        right = s[1:].count('1')
        result = left + right
        for c in s[1:-1]:
            if c == '0':
                left += 1
            else:
                right -= 1
            result = max(result, left + right)
        return result
