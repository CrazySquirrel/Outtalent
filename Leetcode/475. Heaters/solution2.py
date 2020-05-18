class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = [-inf] + sorted(heaters) + [inf]

        i = result = 0

        for house in houses:
            while house >= heaters[i + 1]: i += 1
            result = max(result, min(house - heaters[i], heaters[i + 1] - house))

        return result
