class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        for i, v in enumerate(a):
            if not v and (i == 0 or a[i - 1] == 0) and (i == len(a) - 1 or a[i + 1] == 0):
                n -= 1
                a[i] = 1
        return n <= 0
