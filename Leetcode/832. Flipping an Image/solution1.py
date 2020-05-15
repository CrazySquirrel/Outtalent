class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[(i + 1) % 2 for i in row[::-1]] for row in A]
