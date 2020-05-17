import bisect


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        pivot = bisect.bisect_left(A, 0)
        j = pivot - 1
        i = pivot
        result = []
        while 0 <= j or i < len(A):
            if 0 <= j and i < len(A):
                if abs(A[j]) < abs(A[i]):
                    result.append(A[j] ** 2)
                    j -= 1
                else:
                    result.append(A[i] ** 2)
                    i += 1
            elif 0 <= j:
                result.append(A[j] ** 2)
                j -= 1
            else:
                result.append(A[i] ** 2)
                i += 1
        return result
