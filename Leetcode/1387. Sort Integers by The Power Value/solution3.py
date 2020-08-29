class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x: int) -> int:
            if x == 1: return 0
            if x % 2 == 0: return 1 + power(x // 2)
            return 1 + power(3 * x + 1)

        def partition(a: List[int], l: int, r: int) -> int:
            x = a[r]
            i = l
            for j in range(l, r):
                if a[j] <= x:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[r] = a[r], a[i]
            return i

        def kthSmallest(a: List[int], l: int, r: int, k: int) -> int:
            i = partition(a, l, r)
            if i - l == k - 1: return a[i][1]
            if i - l > k - 1: return kthSmallest(a, l, i - 1, k)
            return kthSmallest(a, i + 1, r, k - i + l - 1)

        return kthSmallest([(power(i), i) for i in range(lo, hi + 1)], 0, hi - lo, k)
