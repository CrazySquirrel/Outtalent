class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origin, dest = map(set, zip(*paths))
        return (dest - origin).pop()
