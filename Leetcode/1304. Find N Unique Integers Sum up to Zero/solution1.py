class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        if n % 2:
            result.append(0)

        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)

        return result
