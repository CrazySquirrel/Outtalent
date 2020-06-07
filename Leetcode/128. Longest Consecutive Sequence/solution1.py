class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 in num_set: continue

            current = 1

            while num + 1 in num_set:
                num += 1
                current += 1

            result = max(result, current)

        return result
