from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1

        for i in range(numCourses):
            zero_degree = False

            for j in range(numCourses):
                if indegrees[j] == 0:
                    zero_degree = True
                    break

            if not zero_degree: return False

            indegrees[j] = -1

            for node in graph[j]: indegrees[node] -= 1

        return True
