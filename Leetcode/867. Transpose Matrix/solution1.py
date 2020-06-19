class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*A)]
