class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda p: p[1])
        curr_pos = points[0][1]
        result = 1
        for x, y in points:
            if curr_pos >= x: continue
            curr_pos = y
            result += 1
        return result
