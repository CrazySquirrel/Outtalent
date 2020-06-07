class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, 0, [], res)
        return res

    def dfs(self, nums, visited, start, subset, res):
        res.append(subset[:])

        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue
            subset.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, i + 1, subset, res)
            subset.pop()
            visited[i] = False
