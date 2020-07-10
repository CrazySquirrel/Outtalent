class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1
        for node in preorder.split(','):
            diff -= 1
            if diff < 0: return False
            if node != '#':  diff += 2
        return diff == 0
