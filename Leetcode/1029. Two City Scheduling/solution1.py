class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result = 0
        costs = sorted(costs, key=lambda x: x[0] - x[1])

        for index in range(len(costs)):
            if index < len(costs) // 2:
                result += costs[index][0]
            else:
                result += costs[index][1]

        return result
