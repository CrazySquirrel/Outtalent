class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = cost[0], cost[1]
        for i in range(2, len(cost)): prev, curr = curr, cost[i] + min(prev, curr)
        return min(prev, curr)
