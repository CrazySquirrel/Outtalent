class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy, first_sell = inf, 0
        second_buy, second_sell = inf, 0

        for price in prices:
            first_buy = min(first_buy, price)
            first_sell = max(first_sell, price - first_buy)

            second_buy = min(second_buy, price - first_sell)
            second_sell = max(second_sell, price - second_buy)

        return second_sell
