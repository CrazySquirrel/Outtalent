class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = -inf

        for n in set(nums):
            if n > m1:
                m3, m2, m1 = m2, m1, n
            elif n > m2:
                m3, m2 = m2, n
            elif n > m3:
                m3 = n

        if m3 > -inf:
            return m3
        else:
            return max(m1, m2, m3)