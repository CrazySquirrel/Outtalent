class Solution:
    def helper(self, s1: str, i: int, s2: str, j: int, r: str, s3: str) -> bool:
        if r == s3 and i == len(s1) and j == len(s2): return True
        if i < len(s1) and self.helper(s1, i + 1, s2, j, r + s1[i], s3): return True
        if j < len(s2) and self.helper(s1, i, s2, j + 1, r + s2[j], s3): return True
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.helper(s1, 0, s2, 0, "", s3)
