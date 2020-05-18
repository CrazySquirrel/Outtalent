class Solution:
    def findUnsortedSubarray(self, nums1: List[int]) -> int:
        nums2 = sorted(nums1)

        start = end = -1

        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i

        return end - start + 1 if start != -1 else 0
