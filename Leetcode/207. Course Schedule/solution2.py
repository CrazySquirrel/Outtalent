from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites: graph[u].append(v)

        visited = [0] * numCourses

        def dfs(i):
            if visited[i] == 1: return False
            if visited[i] == 2: return True

            visited[i] = 1

            for j in graph[i]:
                if not dfs(j): return False

            visited[i] = 2

            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True
