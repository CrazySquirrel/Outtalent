class Solution:
    def jump(self, nums: List[int]) -> int:
        result = reach = max_reach = 0
        for index, num in enumerate(nums):
            if index > reach:
                reach = max_reach
                result += 1
            max_reach = max(max_reach, index + num)
        return result
