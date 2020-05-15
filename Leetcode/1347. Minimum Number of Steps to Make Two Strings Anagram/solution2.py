class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum(max(0, s.count(i) - t.count(i)) for i in set(s))
