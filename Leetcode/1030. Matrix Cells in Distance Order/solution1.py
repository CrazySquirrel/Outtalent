class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([(i, j) for i in range(R) for j in range(C)], key=lambda x: abs(r0 - x[0]) + abs(c0 - x[1]))
