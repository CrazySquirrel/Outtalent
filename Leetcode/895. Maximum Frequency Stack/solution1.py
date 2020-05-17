class FreqStack:

    def __init__(self):
        self.counter = {}
        self.group = {}
        self.max = 0

    def push(self, x: int) -> None:
        if x not in self.counter:
            self.counter[x] = 1
        else:
            self.counter[x] += 1

        freq = self.counter[x]

        if freq not in self.group:
            self.group[freq] = [x]
        else:
            self.group[freq].append(x)

        self.max = max(self.max, freq)

    def pop(self) -> int:
        x = self.group[self.max].pop()

        self.counter[x] -= 1

        if not self.group[self.max]:
            self.max -= 1

        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
