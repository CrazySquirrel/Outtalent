class Solution:
    def dfs(self, candidates: List[int], target: int, index: int, result: List[List[int]], path: List[int]) -> None:
        if target < 0: return None
        if target == 0: return result.append(path)
        for i in range(index, len(candidates)):
            if candidates[i] > target: continue
            self.dfs(candidates, target - candidates[i], i + 1, result, path + [candidates[i]])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, result, [])
        result = set([tuple(sorted(r)) for r in result])
        return [list(r) for r in result]