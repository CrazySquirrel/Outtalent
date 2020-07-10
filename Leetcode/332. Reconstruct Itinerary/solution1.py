from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in tickets: graph[f].append(t)
        for f, ts in graph.items(): ts.sort(reverse=True)

        def dfs(source):
            while graph[source]: dfs(graph[source].pop())
            result.append(source)

        result = []
        dfs('JFK')
        return result[::-1]
