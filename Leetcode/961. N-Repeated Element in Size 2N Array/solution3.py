class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for a in A:
            if a in s:
                return a
            s.add(a)
