from itertools import chain


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return chain(*zip(nums[:n], nums[n:]))
