class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1, n)) + [-1 * (n * (n - 1)) // 2]
