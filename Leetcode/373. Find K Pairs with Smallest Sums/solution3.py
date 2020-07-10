from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []

        result = []

        l1, l2 = len(nums1), len(nums2)

        q = [(nums1[i] + nums2[0], nums1[i], nums2[0], 0) for i in range(len(nums1))]

        while q and k:
            t0, t1, t2, t3 = heappop(q)
            result.append([t1, t2])
            if t3 < l2 - 1: heappush(q, (t1 + nums2[t3 + 1], t1, nums2[t3 + 1], t3 + 1))
            k -= 1

        return result
