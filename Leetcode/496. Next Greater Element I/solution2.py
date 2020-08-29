class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        grater = []
        for n in nums2[::-1]:
            while grater and grater[-1] < n: grater.pop()
            h[n] = grater[-1] if grater else -1
            grater.append(n)
        return [h[n] for n in nums1]
