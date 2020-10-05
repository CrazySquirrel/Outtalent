class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 2003
        self.nums = [[] for _ in range(self.base + 1)]

    def hash(self, val: int) -> int:
        return val % self.base

    def add(self, val: int) -> None:
        key = self.hash(val)
        if val not in self.nums[key]: self.nums[key].append(val)

    def remove(self, val: int) -> None:
        key = self.hash(val)
        if val in self.nums[key]: self.nums[key].remove(val)

    def contains(self, val: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        key = self.hash(val)
        return val in self.nums[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
