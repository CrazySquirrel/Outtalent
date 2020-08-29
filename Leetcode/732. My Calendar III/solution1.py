from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.delta = Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1

        active = result = 0

        for x in sorted(self.delta):
            active += self.delta[x]
            result = max(result, active)

        return result

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
