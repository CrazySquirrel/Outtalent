class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lens = len(nums1) + len(nums2)
        if lens % 2 == 1:
            return self.kthSmallest(nums1, nums2, lens // 2)
        else:
            return (self.kthSmallest(nums1, nums2, lens // 2 - 1) + self.kthSmallest(nums1, nums2, lens // 2)) / 2.0

    def kthSmallest(self, nums1: List[int], nums2: List[int], k: int) -> float:
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        midIdx1, midIdx2 = len(nums1) // 2, len(nums2) // 2
        midVal1, midVal2 = nums1[midIdx1], nums2[midIdx2]

        if k > midIdx1 + midIdx2:
            if midVal1 < midVal2:
                return self.kthSmallest(nums1[midIdx1 + 1:], nums2, k - midIdx1 - 1)
            else:
                return self.kthSmallest(nums1, nums2[midIdx2 + 1:], k - midIdx2 - 1)
        else:
            if midVal1 > midVal2:
                return self.kthSmallest(nums1[:midIdx1], nums2, k)
            else:
                return self.kthSmallest(nums1, nums2[:midIdx2], k)
