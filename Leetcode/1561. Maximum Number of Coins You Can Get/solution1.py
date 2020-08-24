class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:int(len(piles) * 2 / 3):2])
