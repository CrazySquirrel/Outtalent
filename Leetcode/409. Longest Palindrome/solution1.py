from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        for c in Counter(s).values():
            result += c // 2 * 2
            if result % 2 == 0 and c % 2 == 1: result += 1
        return result
