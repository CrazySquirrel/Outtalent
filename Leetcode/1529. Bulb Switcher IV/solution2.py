class Solution:
    def minFlips(self, target: str) -> int:
        return 2 * target.count('10') + (target[-1] == '1')
