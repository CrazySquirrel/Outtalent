class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k > 0:
            for i, v in enumerate(nums[-k:] + nums[0:-k]):
                nums[i] = v
