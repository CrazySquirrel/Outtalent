class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums) // 3
        counter = collections.Counter()
        result = set()
        for n in nums:
            counter[n] += 1
            if counter[n] > l: result.add(n)
        return result
