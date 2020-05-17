class Solution:
    def dfs(self, node, visited, cur):
        if node == self.n:
            yield cur
        else:
            for v in self.graph[node]:
                if v not in visited:
                    visited.add(v)
                    yield from self.dfs(v, visited, cur + [v])
                    visited.remove(v)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.n = len(graph) - 1

        return list(self.dfs(0, set(), [0]))
