class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = index = 0

        while index < len(heights):
            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)

        return max_area
