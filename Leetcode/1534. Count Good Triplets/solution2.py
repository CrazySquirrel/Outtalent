class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)

        ij_idx = [set() for _ in range(n)]
        jk_ids = [set() for _ in range(n)]
        ik_ids = [set() for _ in range(n)]

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                d = abs(arr[j] - arr[i])
                if d <= a: ij_idx[i].add(j)
                if d <= b: jk_ids[i].add(j)
                if d <= c: ik_ids[j].add(i)

        result = 0

        for i in range(n - 2):
            for j in ij_idx[i]:
                for k in jk_ids[j]:
                    if i in ik_ids[k]:
                        result += 1

        return result
