class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            result += 1
            numBottles += 1
        return result