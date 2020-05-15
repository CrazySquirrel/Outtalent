class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]

        result = []

        for query in queries:
            index = p.index(query)
            result.append(index)
            p.insert(0, p.pop(index))

        return result
