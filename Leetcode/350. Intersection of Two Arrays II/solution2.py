from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []
        for n in counter1:
            if n in counter2:
                result.extend([n] * min(counter1[n], counter2[n]))
        return result
