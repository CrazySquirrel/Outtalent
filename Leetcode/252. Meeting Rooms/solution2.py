class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(e2 <= s1 for (s1, e1), (s2, e2) in zip(intervals[1:], intervals[:-1]))
