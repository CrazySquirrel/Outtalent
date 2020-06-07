class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x1, y1 in points:
            dist = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2: continue
                dx = x1 - x2
                dy = y1 - y2
                d = dx * dx + dy * dy
                if d in dist:
                    ans += dist[d]
                    dist[d] += 1
                else:
                    dist[d] = 1
        return ans * 2
