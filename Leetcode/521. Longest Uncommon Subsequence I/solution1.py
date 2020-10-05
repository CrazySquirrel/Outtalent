class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        la, lb = len(a), len(b)
        if la < lb: return lb
        if la > lb: return la
        return la if a != b else -1
