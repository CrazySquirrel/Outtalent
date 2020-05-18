from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        if k == 0:
            return sum([counter[num] > 1 for num in counter])
        elif k > 0:
            return sum([num + k in counter for num in set(nums)])
        else:
            return 0
