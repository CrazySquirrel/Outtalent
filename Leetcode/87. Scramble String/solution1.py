class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 0: return True
        if len(s1) == 1: return s1 == s2
        if sorted(s1) != sorted(s2): return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]): return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]): return True
        return False
