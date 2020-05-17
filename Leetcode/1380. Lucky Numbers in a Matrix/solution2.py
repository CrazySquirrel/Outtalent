class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minr = set(min(row) for row in matrix)
        maxc = set(max(col) for col in zip(*matrix))
        return list(minr & maxc)
