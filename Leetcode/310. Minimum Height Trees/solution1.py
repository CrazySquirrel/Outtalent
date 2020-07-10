class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0: return []
        if n == 1: return [0]

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = collections.deque()
        for u, vs in graph.items():
            if len(vs) == 1: queue.append(u)

        while n > 2:
            l = len(queue)
            n -= l
            for _ in range(l):
                u = queue.popleft()
                for v in graph[u]:
                    graph[v].remove(u)
                    if len(graph[v]) == 1:
                        queue.append(v)

        return list(queue)
