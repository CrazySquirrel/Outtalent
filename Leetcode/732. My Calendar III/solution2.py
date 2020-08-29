from bisect import insort_left, bisect_left, bisect_right


class MyCalendarThree:

    def __init__(self):
        self.starts = []
        self.ends = []
        self.counter = 0

    def book(self, start: int, end: int) -> int:
        insort_left(self.starts, start)
        insort_left(self.ends, end)
        l, r = bisect_left(self.starts, start), bisect_left(self.starts, end)
        for i, val in enumerate(self.starts[l:r], start=l):
            j = bisect_right(self.ends, val)
            self.counter = max(self.counter, i + 1 - j)
        return self.counter

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
