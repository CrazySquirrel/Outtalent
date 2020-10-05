class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ranks = {num: r + 1 for r, num in enumerate(sorted(nums, reverse=True))}
        map_rank = lambda r: ["Gold Medal", "Silver Medal", "Bronze Medal"][r - 1] if r <= 3 else str(r)
        return [map_rank(ranks[num]) for num in nums]
