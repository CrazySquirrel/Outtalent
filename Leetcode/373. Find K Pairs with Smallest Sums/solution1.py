class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = sorted([(n1, n2, n1 + n2) for n1 in nums1 for n2 in nums2], key=lambda x: x[2])
        return [(n1, n2) for n1, n2, s in result[:k]]
