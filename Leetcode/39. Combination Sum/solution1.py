class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for c in candidates:
            if c == target:
                result.append([c])
            elif c < target:
                for r in self.combinationSum(candidates, target - c):
                    result.append([c] + r)

        result = set([tuple(sorted(r)) for r in result])

        return [list(r) for r in result]
