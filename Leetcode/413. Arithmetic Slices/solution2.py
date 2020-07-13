class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        counter = result = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                counter += 1
            else:
                result += (counter + 1) * counter // 2
                counter = 0
        result += (counter + 1) * counter // 2
        return result
