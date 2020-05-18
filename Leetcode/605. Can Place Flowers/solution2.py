class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        i, l1, l2 = 0, len(flowerbed), len(flowerbed) - 1
        while n > 0 and i < l1:
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == l2 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 1
        return n == 0
