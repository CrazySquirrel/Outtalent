class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        if not mat and not mat[0]: return 0

        rows = defaultdict(int)
        cols = defaultdict(int)

        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if mat[i][j]:
                    rows[i] += mat[i][j]
                    cols[j] += mat[i][j]

        result = 0

        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if mat[i][j] == rows[i] == cols[j] == 1:
                    result += 1

        return result
