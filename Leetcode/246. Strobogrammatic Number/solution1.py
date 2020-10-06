class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotates = [0, 1, None, None, None, None, 9, None, 8, 6]
        for n1, n2 in zip(map(int, num), map(int, num[::-1])):
            if n1 != rotates[n2] or n2 != rotates[n1]: return False
        return True
