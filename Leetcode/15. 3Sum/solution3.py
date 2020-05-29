class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = {}
        three_sum = {}

        for i in range(len(nums)):
            for value in two_sum.get(-nums[i], {}).values():
                tmp = sorted(value + [nums[i]])
                three_sum["%d,%d,%d" % (tmp[0], tmp[1], tmp[2])] = tmp

            for j in range(i):
                add_value = nums[i] + nums[j]
                two_sum[add_value] = two_sum.get(add_value, {})
                key = (nums[j], nums[i]) if nums[j] < nums[i] else (nums[i], nums[j])
                two_sum[add_value]["%d,%d" % key] = [nums[j], nums[i]]

        return [v for k, v in three_sum.items()]
