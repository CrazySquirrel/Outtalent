class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        M, N = len(num1), len(num2)

        if M < N:
            num1 = "0" * (N - M) + num1
        else:
            num2 = "0" * (M - N) + num2

        N = max(M, N)

        result = ''
        carry = 0

        for i in range(N - 1, -1, -1):
            carry += ord(num1[i]) + ord(num2[i]) - 2 * ord('0')
            result = chr(carry % 10 + ord('0')) + result
            carry //= 10

        if carry:
            result = '1' + result

        return result
