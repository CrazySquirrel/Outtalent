from collections import Counter
from heapq import heappush, heappushpop, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt = [(v[1], v[0]) for v in cnt.items()]

        pq = []
        for v in cnt:
            if len(pq) < k:
                heappush(pq, v)
            else:
                heappushpop(pq, v)

        result = []
        while pq: result.append(heappop(pq)[1])
        return result[::-1]
