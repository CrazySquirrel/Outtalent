class Solution:
    def getRows(self, x: str, y: str, z: str) -> List[List[str]]:
        colors = {'R', 'G', 'Y'}
        result = []

        for i in colors - {x}:
            for j in colors - {i, y}:
                for k in colors - {j, z}:
                    result.append((i, j, k))

        return result

    def numOfWays(self, n: int) -> int:
        rows = self.getRows('', '', '')

        counter = len(rows)

        for i in range(1, n):
            next_rows = []
            for row in rows:
                next_rows.extend(self.getRows(row[0], row[1], row[2]))
            counter = len(next_rows)
            rows = next_rows

        return int(counter % (1e9 + 7))
