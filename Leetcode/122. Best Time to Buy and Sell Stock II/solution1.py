class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, l = 0, len(prices) - 1
        max_profit = 0
        while i < l:
            while i < l and prices[i] >= prices[i + 1]: i += 1
            valley = prices[i]
            while i < l and prices[i] <= prices[i + 1]: i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit
