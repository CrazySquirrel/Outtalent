from collections import Counter


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        half_sum, sums, result = sum(nums) // 2, 0, []
        counter = Counter(nums)
        for i in range(100, 0, -1):
            while counter[i] > 0 and sums <= half_sum:
                counter[i] -= 1
                sums += i
                result.append(i)
        return result
