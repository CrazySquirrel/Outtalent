from collections import defaultdict


class Solution:
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)

    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        for i in range(N):
            lines = defaultdict(int)
            duplicates = 1
            for j in range(i + 1, N):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                delta = self.gcd(dx, dy)
                lines[(dx // delta, dy // delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res
