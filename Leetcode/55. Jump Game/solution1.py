class Solution:
    def canJumpFromPosition(self, position: int, nums: List[int]) -> bool:
        if position == len(nums) - 1: return True

        furthest_jump = min(position + nums[position], len(nums) - 1)

        for nextPosition in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(nextPosition, nums): return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpFromPosition(0, nums)
