class Solution:
    def canJumpFromPosition(self, position: int, nums: List[int]) -> bool:
        if self.memo[position] != None:
            return self.memo[position]

        furthest_jump = min(position + nums[position], len(nums) - 1)

        for nextPosition in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                self.memo[position] = True
                return True

        self.memo[position] = False
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.memo = [None] * len(nums)
        self.memo[-1] = True
        return self.canJumpFromPosition(0, nums)
