from bisect import bisect_right


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        h = {}

        for i, (start, end) in enumerate(intervals):
            if start not in h: h[start] = i

        starts = list(sorted(h))

        result = []

        for start, end in intervals:
            if end in h:
                result.append(h[end])
            elif end > starts[-1]:
                result.append(-1)
            else:
                result.append(h[starts[bisect_right(starts, end)]])

        return result
