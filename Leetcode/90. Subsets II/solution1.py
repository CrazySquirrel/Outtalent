class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        for i in range(0, 2 ** n):
            bitmask = '{:0{width}b}'.format(i, width=n)
            result.add(tuple(sorted(nums[j] for j in range(n) if bitmask[j] == '1')))
        return result
