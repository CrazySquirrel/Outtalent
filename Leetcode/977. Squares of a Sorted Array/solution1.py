class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(a ** 2 for a in A)
