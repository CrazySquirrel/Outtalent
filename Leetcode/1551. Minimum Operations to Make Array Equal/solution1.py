class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n * (n // 2)) // 2
        else:
            return ((n + 1) * ((n - 1) // 2)) // 2
