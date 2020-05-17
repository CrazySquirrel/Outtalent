class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, result, l = [[0]], [], len(graph) - 1

        while paths:
            path = paths.pop()

            for node in graph[path[-1]]:
                if node == l:
                    result.append(path + [node])
                else:
                    paths.append(path + [node])

        return result
