class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        result = []
        for n1 in nums1:
            for n2 in nums2:
                n = (n1 + n2, n1, n2)
                i = bisect.bisect_left(result, n)
                if i >= k: break
                bisect.insort(result, n)
            result = result[:k]
        return [(n1, n2) for s, n1, n2, in result]
