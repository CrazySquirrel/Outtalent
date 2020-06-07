class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n

            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True

        return False
