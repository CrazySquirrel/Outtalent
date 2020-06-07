class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        heights.pop()
        return result

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        M, N = len(matrix), len(matrix[0])
        height = [0] * N
        res = 0

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            res = max(res, self.largestRectangleArea(height))

        return res
