class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1 = m2 = inf
        for n in nums:
            if n <= m1: m1 = n
            elif n <= m2: m2 = n
            else: return True
        return False
