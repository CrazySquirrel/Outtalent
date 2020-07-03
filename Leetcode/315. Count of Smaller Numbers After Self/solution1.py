from bisect import bisect_left


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, temp = [0] * n, []
        for j in range(n - 1, -1, -1):
            i = bisect_left(temp, nums[j])
            res[j] = i
            temp[i:i] = [nums[j]]
        return res
