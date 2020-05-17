class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, i, l = [[0]], 0, len(graph) - 1

        while i < len(paths):
            path = paths.pop()

            for node in graph[path[-1]]:
                if node == l:
                    paths.insert(0, path + [node])
                    i += 1
                else:
                    paths.append(path + [node])

        return paths
