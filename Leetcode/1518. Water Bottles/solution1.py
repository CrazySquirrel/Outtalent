class Solution:
    def numWaterBottles(self, numFullBottles: int, numExchange: int) -> int:
        numEmptyBottles = 0
        result = 0
        while numFullBottles > 0:
            result += numFullBottles
            numEmptyBottles += numFullBottles
            numFullBottles = (int)(numEmptyBottles / numExchange)
            numEmptyBottles -= numFullBottles * numExchange
        return result
