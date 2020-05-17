from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.buckets = defaultdict(list)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, x: int) -> None:
        current = self.freq[x] + 1
        self.freq[x] = current
        self.max_freq = max(self.max_freq, current)
        self.buckets[current].append(x)

    def pop(self) -> int:
        bucket = self.buckets[self.max_freq]
        result = bucket.pop()
        if not bucket: self.max_freq -= 1
        self.freq[result] -= 1
        return result

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
