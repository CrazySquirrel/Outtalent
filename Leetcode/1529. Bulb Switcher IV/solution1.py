class Solution:
    def minFlips(self, target: str) -> int:
        result = 0
        t = 1
        for c in target:
            if c == t:
                t ^= 1
                result += 1
        return result
