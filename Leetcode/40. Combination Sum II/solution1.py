class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)

        def dfs(target: int, index: int, path: List[int]) -> None:
            if target < 0: return None
            if target == 0: return result.append(path)
            for i in range(index, l):
                if candidates[i] > target: break
                if i > index and candidates[i - 1] == candidates[i]: continue
                dfs(target - candidates[i], i + 1, path + [candidates[i]])

        result = []
        candidates.sort()

        dfs(target, 0, [])

        return result
