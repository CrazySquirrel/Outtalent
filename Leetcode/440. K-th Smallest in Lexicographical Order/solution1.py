class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k > 0:
            step, first, last = 0, cur, cur + 1

            while first <= n:
                step += min(last, n + 1) - first
                first *= 10
                last *= 10

            if k >= step:
                k -= step
                cur += 1
            else:
                cur *= 10
                k -= 1

        return cur
