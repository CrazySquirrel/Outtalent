class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = collections.Counter()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.counter[key] += 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if self.counter[key] > 1:
            self.counter[key] -= 1
        elif self.counter[key] == 1:
            del self.counter[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if len(self.counter) == 0: return ''
        return max(self.counter, key=lambda x: self.counter[x])

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if len(self.counter) == 0: return ''
        return min(self.counter, key=lambda x: self.counter[x])

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
