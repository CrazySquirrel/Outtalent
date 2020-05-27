class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x_left, x_right = newInterval
        left, right = [], []

        for start, end in intervals:
            if start > x_right:
                right.append([start, end])
            elif end < x_left:
                left.append([start, end])
            else:
                x_left = min(start, x_left)
                x_right = max(end, x_right)

        return left + [[x_left, x_right]] + right
