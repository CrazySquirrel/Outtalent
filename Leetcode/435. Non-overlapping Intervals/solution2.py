class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[1])
        last = intervals[0]
        result = 0
        for interval in intervals[1:]:
            if interval[0] >= last[1]:
                last = interval
            else:
                result += 1
        return result
