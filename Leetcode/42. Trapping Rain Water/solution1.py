class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        result = 0

        for i in range(1, len(height) - 1):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            result += min(left_max, right_max) - height[i]

        return result
