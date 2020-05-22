class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        i = j = k = 0
        while i < len(nums2) and j < len(nums3):
            if nums2[i] <= nums3[j]:
                nums1[k] = nums2[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums3[j]
                j += 1
                k += 1
        if i < len(nums2):
            nums1[k:] = nums2[i:]
        if j < len(nums3):
            nums1[k:] = nums3[j:]
