class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None] * maxSize
        self.maxSize = maxSize
        self.top = 0

    def push(self, x: int) -> None:
        if self.top == self.maxSize: return
        self.stack[self.top] = x
        self.top += 1

    def pop(self) -> int:
        if self.top == 0: return -1
        self.top -= 1
        result = self.stack[self.top]
        self.stack[self.top] = None
        return result

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(k, self.top)): self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
