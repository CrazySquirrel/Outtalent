class Solution:
    def traverse(self, nums: List[List[int]]):
        for row in nums:
            for cell in row:
                yield cell

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c: return nums

        nums = self.traverse(nums)
        result = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                result[i][j] = nums.__next__()

        return result
