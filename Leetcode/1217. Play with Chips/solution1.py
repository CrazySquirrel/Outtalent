class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        O = E = 0
        for x in chips:
            if x % 2 == 0:
                E += 1
            else:
                O += 1
        return min(E, O)
