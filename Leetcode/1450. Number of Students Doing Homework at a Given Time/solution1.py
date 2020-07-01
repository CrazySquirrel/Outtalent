class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum((t1 <= queryTime <= t2) for t1, t2 in zip(startTime, endTime))
