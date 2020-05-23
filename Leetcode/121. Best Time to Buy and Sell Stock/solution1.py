class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        mn, mx = prices[0], 0
        for p in prices: mn, mx = min(mn, p), max(mx, p - mn)
        return mx
