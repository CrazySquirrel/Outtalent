class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        paths = {(0,)}
        l = len(graph) - 1

        while paths:
            new_paths = set()

            for path in paths:
                for node in graph[path[-1]]:
                    if node == l:
                        result.append(path + (node,))
                    else:
                        new_paths.add(path + (node,))

            paths = new_paths

        return result
