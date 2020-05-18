from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0
        for num in set(nums):
            if k > 0 and num + k in counter:
                result += 1
            elif k == 0 and counter[num] > 1:
                result += 1
        return result