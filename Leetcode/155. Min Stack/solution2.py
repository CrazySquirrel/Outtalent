class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = inf

    def push(self, x: int) -> None:
        self.min = min(self.min, x)
        self.stack.append((x, self.min))

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[-1][1] if self.stack else inf

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
