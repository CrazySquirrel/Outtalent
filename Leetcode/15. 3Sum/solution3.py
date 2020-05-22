class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = {}
        three_sum = {}

        for i in range(len(nums)):
            two_dict = two_sum.get(0 - nums[i], None)
            if two_dict:
                for key, value in two_dict.items():
                    tmp = sorted(value + [nums[i]])
                    three_sum["%d,%d,%d" % (tmp[0], tmp[1], tmp[2])] = tmp
            j = 0
            while j < i:
                add_value = nums[i] + nums[j]
                if not two_sum.get(add_value): two_sum[add_value] = {}
                key = (nums[j], nums[i]) if nums[j] < nums[i] else (nums[i], nums[j])
                two_sum[add_value]["%s,%s" % key] = [nums[j], nums[i]]
                j += 1

        return [v for k, v in three_sum.items()]
