class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    result.append(prices[i] - prices[j])
                    break
            else:
                result.append(prices[i])
        return result
