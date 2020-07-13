class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        l = len(A)

        if l < 3: return 0

        result = 0
        for i in range(0, l - 2):
            k = A[i + 1] - A[i]
            for j in range(i + 2, l):
                if A[j] - A[j - 1] != k: break
                result += 1

        return result
