class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result = 0
        for col in zip(*A):
            if any(col[i] > col[i + 1] for i in range(len(col) - 1)): result += 1
        return result
