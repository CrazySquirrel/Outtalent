class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotates = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        m = len(num) // 2
        for n1, n2 in zip(num[:m + 1], num[m:][::-1]):
            if n1 not in rotates or n2 not in rotates or n1 != rotates[n2] or n2 != rotates[n1]: return False
        return True
