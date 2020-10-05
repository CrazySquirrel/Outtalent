class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0

        pref = nums[0]
        counter = result = 1

        for num in nums:
            if pref >= num:
                result = max(result, counter)
                counter = 1
            else:
                counter += 1

            pref = num

        return max(result, counter)
