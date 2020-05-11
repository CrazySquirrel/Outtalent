class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        result = 0
        accumulate = 0

        for rate in satisfaction:
            if rate + accumulate < 0: break
            accumulate += rate
            result += accumulate

        return result
