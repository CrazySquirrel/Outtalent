class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def solve(l1, r1, l2, r2):
            if r1 - l1 == 1: return s1[l1] == s2[l2]
            if sorted(s1[l1:r1]) != sorted(s2[l2:r2]): return False
            for k in range(1, r1 - l1):
                if solve(l1, l1 + k, l2, l2 + k) and solve(l1 + k, r1, l2 + k, r2): return True
                if solve(l1, l1 + k, r2 - k, r2) and solve(l1 + k, r1, l2, r2 - k): return True

        return solve(0, len(s1), 0, len(s2))
