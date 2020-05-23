class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices))])
