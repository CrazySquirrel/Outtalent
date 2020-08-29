from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m > n: return self.numSubmatrixSumTarget(list(map(list, zip(*matrix))), target)

        for i in range(m):
            for j in range(len(matrix[i]) - 1):
                matrix[i][j + 1] += matrix[i][j]

        result = 0

        for i in range(m):
            prefix_sum = [0] * len(matrix[i])

            for j in range(i, m):
                lookup = defaultdict(int)
                lookup[0] = 1

                for k in range(len(matrix[j])):
                    prefix_sum[k] += matrix[j][k]

                    if prefix_sum[k] - target in lookup:
                        result += lookup[prefix_sum[k] - target]

                    lookup[prefix_sum[k]] += 1

        return result
