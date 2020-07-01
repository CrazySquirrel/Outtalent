class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([x[int(i >= len(costs) // 2)] for i, x in enumerate(sorted(costs, key=lambda x: (x[0] - x[1])))])
