class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 2:
            return points

        def orient(p1, p2, p3):
            return (p2[1] - p3[1]) * (p1[0] - p3[0]) - (p1[1] - p3[1]) * (p2[0] - p3[0])

        points.sort(key=lambda x: (x[0], -x[1]))

        bottom = points[0:2]

        for p in points[2:]:
            while len(bottom) >= 2 and orient(bottom[-2], bottom[-1], p) < 0: bottom.pop()
            bottom.append(p)

        top = points[::-1][0:2]

        for p in points[::-1][2:]:
            while len(top) >= 2 and orient(top[-2], top[-1], p) < 0: top.pop()
            top.append(p)

        return list(set([(i, j) for i, j in bottom + top[1:-1]]))
