class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            m = total % k if k else total
            if m not in h:
                h[m] = i
            elif h[m] + 1 < i:
                return True
        return False
