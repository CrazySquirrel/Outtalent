class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = {}
        left = {}
        right = {}

        max_frequency = 0

        for i, v in enumerate(nums):
            if v not in counter:
                counter[v] = 1
                left[v] = i
                right[v] = i
            else:
                right[v] = i
                counter[v] += 1

            max_frequency = max(max_frequency, counter[v])

        result = inf

        for c in counter:
            if counter[c] == max_frequency:
                result = min(result, right[c] - left[c] + 1)

        return result
