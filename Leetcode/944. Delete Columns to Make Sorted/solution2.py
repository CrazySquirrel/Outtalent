class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(list(column) != sorted(column) for column in zip(*A))
