class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        i = len(A) - 1

        while i > 0 and A[i] > 9:
            A[i - 1] += A[i] // 10
            A[i] %= 10
            i -= 1

        while A[0] > 9:
            A.insert(0, A[0] // 10)
            A[1] %= 10

        return A
