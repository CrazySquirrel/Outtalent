class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        if s <= e:
            return list(range(s, e + 1))
        else:
            return list(range(1, e + 1)) + list(range(s, n + 1))
