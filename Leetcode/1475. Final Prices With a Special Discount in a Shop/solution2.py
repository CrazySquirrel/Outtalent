class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
