class Solution:
    def dfs(self, candidates: List[int], target: int, index: int, result: List[List[int]], path: List[int]) -> None:
        if target < 0: return None
        if target == 0: return result.append(path)
        for i in range(index, len(candidates)):
            if candidates[i] > target: continue
            self.dfs(candidates, target - candidates[i], i, result, path + [candidates[i]])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, result, [])
        return result
