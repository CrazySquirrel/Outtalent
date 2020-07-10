class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0

        peak_mask = [[0x7FFFFFFF] * n for _ in range(m)]

        q = []

        for x in range(m):
            for y in range(n):
                if x in (0, m - 1) or y in (0, n - 1):
                    peak_mask[x][y] = heightMap[x][y]
                    q.append((x, y))

        while q:
            x, y = q.pop(0)

            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy

                if nx <= 0 or nx >= m - 1 or ny <= 0 or ny >= n - 1: continue

                limit = max(peak_mask[x][y], heightMap[nx][ny])

                if peak_mask[nx][ny] > limit:
                    peak_mask[nx][ny] = limit
                    q.append((nx, ny))

        return sum(peak_mask[x][y] - heightMap[x][y] for x in range(m) for y in range(n))
