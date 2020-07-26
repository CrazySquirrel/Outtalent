class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0] * 26
        curr = 1
        expected_code = None

        for i, c in enumerate(p):
            char_code = ord(c) - ord('a')

            if char_code == expected_code:
                curr += 1
            else:
                curr = 1

            dp[char_code] = max(dp[char_code], curr)

            if char_code == 25:
                expected_code = 0
            else:
                expected_code = char_code + 1

        return sum(dp)
