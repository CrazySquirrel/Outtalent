from collections import defaultdict


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)

        ij_idx = defaultdict(set)
        jk_ids = defaultdict(set)
        ik_ids = defaultdict(set)

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                d = abs(arr[j] - arr[i])
                if d <= a: ij_idx[i].add(j)
                if d <= b: jk_ids[i].add(j)
                if d <= c: ik_ids[j].add(i)

        return sum([i in ik_ids[k] for i in ij_idx for j in ij_idx[i] for k in jk_ids[j]])
