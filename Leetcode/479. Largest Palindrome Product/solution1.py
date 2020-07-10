class Solution:
    def largestPalindrome(self, n: int) -> int:
        upper = 10 ** n - 1
        lower = upper // 10
        for i in range(upper, lower, -1):
            l = int(str(i) + str(i)[::-1])
            j = upper
            while j * j > l:
                if l % j == 0: return l % 1337
                j -= 1
        return 9
