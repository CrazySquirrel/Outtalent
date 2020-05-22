class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = set()
        nums.sort()
        for i in range(0,length-2):
            j = i + 1
            k = length - 1
            while j < k:
                sum0 = nums[i] + nums[j] + nums[k]
                if sum0 == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j +=1
                elif sum0 < 0: j +=1
                elif sum0 > 0: k -=1
        return result