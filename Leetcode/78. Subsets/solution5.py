class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(0, 2 ** n):
            bitmask = '{:0{width}b}'.format(i, width=n)
            result.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return result
