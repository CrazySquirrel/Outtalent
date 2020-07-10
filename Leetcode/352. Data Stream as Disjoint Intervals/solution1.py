class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        bisect.insort(self.intervals, (val, val))
        i = bisect.bisect_left(self.intervals, (val, val))
        s, e = max(0, i - 1), min(i + 2, len(self.intervals))
        self.intervals[s:e] = self.merge(self.intervals[s:e])

    def merge(self, ints: List[List[int]]) -> List[List[int]]:
        if len(ints) == 1: return ints

        if len(ints) > 1 and ints[1][0] - ints[0][1] <= 1:
            ints[1] = (min(ints[0][0], ints[1][0]), max(ints[0][1], ints[1][1]))
            ints.pop(0)

        if len(ints) > 1 and ints[-1][0] - ints[-2][1] <= 1:
            ints[-2] = (min(ints[-2][0], ints[-1][0]), max(ints[-2][1], ints[-1][1]))
            ints.pop()

        return ints

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
