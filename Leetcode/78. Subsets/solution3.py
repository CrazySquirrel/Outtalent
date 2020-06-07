class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                result.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        result = []
        n = len(nums)

        for k in range(n + 1):
            backtrack()

        return result
