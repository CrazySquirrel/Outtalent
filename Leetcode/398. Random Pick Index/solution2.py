class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.l = len(nums)

    def pick(self, target: int) -> int:
        return random.choice([i for i in range(self.l) if self.nums[i] == target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
