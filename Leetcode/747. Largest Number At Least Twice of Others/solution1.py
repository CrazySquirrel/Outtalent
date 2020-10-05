class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1 = m2 = mi = 0
        for i, v in enumerate(nums):
            if v > m1:
                m2, m1, mi = m1, v, i
            elif v > m2:
                m2 = v
        return mi if m1 >= m2 * 2 else -1
