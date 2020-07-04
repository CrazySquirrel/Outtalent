class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        s = []

        result = 0

        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                top = s.pop()
                if not s: break
                distance = i - s[-1] - 1
                bounded_height = min(height[i], height[s[-1]]) - height[top]
                result += distance * bounded_height
            s.append(i)

        return result
