class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        s = nums2[:1]
        for num in nums2[1:]:
            while s and s[-1] < num: h[s.pop()] = num
            s.append(num)
        return [h.get(num, -1) for num in nums1]
