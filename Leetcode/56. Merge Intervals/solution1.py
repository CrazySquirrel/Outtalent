class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        i = 1

        while i < len(intervals):
            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i - 1][0] = min(intervals[i - 1][0], intervals[i][0])
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1

        return intervals
