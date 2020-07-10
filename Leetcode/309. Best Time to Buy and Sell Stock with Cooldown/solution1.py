class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        hold, nothold, cooldown = -prices[0], 0, -inf
        for i in range(1, len(prices)):
            hold, nothold, cooldown = max(hold, nothold - prices[i]), max(nothold, cooldown), hold + prices[i]
        return max(nothold, cooldown, hold)
