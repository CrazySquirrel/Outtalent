class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        cook = []
        result = 0
        length = 0

        while satisfaction:
            cook.append(satisfaction.pop())
            length += 1
            cur = sum([cook[i] * (length - i) for i in range(length)])
            if result < cur:
                result = cur
            else:
                break

        return result
