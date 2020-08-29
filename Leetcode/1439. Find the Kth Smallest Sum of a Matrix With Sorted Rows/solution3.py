from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        n1, n2 = len(nums1), len(nums2)
        pq = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        while pq and k:
            s, i, j = heappop(pq)
            res.append(s)
            if i == 0 and j + 1 < n2:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            if i + 1 < n1:
                heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
            k -= 1
        return res

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        res = mat[0]
        for i in range(1, m):
            res = self.kSmallestPairs(res, mat[i], k)
        return res[k - 1]
