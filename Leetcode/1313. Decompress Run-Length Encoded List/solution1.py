class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])

        return result
