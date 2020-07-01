class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        graph = [[] for i in range(N)]

        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        for i in range(N):
            colors = {1, 2, 3, 4}

            for j in graph[i]:
                if res[j] in colors: colors.remove(res[j])

            res[i] = colors.pop()

        return res
