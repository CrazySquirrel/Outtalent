class Solution:
    def flip(self, mat: List[List[int]], w: int, h: int, i: int, j: int) -> List[List[int]]:
        for (di, dj) in ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < h and 0 <= nj < w:
                mat[ni][nj] = (mat[ni][nj] + 1) % 2
        return mat

    def minFlips(self, mat: List[List[int]]) -> int:
        w, h = len(mat[0]), len(mat)

        best = 10000

        for x in range(1 << h):
            cur = [[c for c in h] for h in mat]

            count = 0

            for c in range(w):
                if (x & (1 << c)) > 0:
                    self.flip(cur, w, h, 0, c)
                    count += 1

            for r in range(1, h):
                for c in range(w):
                    if cur[r - 1][c] == 1:
                        self.flip(cur, w, h, r, c)
                        count += 1

            if all(cur[i][j] == 0 for j in range(w) for i in range(h)):
                best = min(best, count)

        return best if best != 10000 else -1
