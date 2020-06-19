class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n < 2 or k < 1: return 0

        if k > n // 2:
            profit = 0
            for i in range(1, n): profit += max(0, prices[i] - prices[i - 1])
            return profit

        buy = [-inf] * k
        sell = [0] * k

        for i in range(n):
            for j in range(k):
                buy[j] = max(buy[j], (sell[j - 1] if j > 0 else 0) - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])

        return sell[-1]
