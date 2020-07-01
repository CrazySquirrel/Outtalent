class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for v, i in sorted([(sum(v), i) for i, v in enumerate(mat)])[:k]]
