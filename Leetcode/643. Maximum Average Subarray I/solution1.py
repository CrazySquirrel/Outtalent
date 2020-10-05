class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums)) / k
