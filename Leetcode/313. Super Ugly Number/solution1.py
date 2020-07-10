from heapq import heappop, heappush


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]

        for _ in range(n - 1):
            ugly = heappop(heap)
            for p in primes:
                heappush(heap, ugly * p)
                if ugly % p == 0: break

        return heap[0]
