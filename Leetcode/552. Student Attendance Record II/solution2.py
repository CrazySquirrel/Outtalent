class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = dp01 = dp10 = 1
        dp11 = dp02 = dp12 = 0

        for i in range(n):
            dp00, dp01, dp02 = (dp00 + dp01 + dp02) % (10 ** 9 + 7), dp00, dp01
            dp10, dp11, dp12 = (dp00 + dp10 + dp11 + dp12) % (10 ** 9 + 7), dp10, dp11

        return dp10
