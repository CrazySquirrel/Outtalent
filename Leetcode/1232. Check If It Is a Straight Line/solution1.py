class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        coordinates = [(x, y) for x, y in coordinates if x != x0 or y != y0]
        slopes = [(y - y0) / (x - x0) if x != x0 else None for x, y in coordinates]
        return all(s == slopes[0] for s in slopes)
