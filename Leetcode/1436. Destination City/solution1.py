class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()

        for path in paths:
            s.add(path[0])
            s.add(path[1])

        for path in paths:
            s.remove(path[0])

        return list(s).pop()
