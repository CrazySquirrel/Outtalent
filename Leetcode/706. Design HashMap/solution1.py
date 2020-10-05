class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 997
        self.map = [[] for _ in range(self.base)]

    def hash(self, key):
        return key % self.base

    def pos(self, key):
        return key // self.base

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = self.hash(key)
        if not self.map[hash_key]: self.map[hash_key] = [None] * self.base
        self.map[hash_key][self.pos(key)] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self.hash(key)
        if (not self.map[hash_key]) or self.map[hash_key][self.pos(key)] == None:
            return -1
        else:
            return self.map[hash_key][self.pos(key)]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self.hash(key)
        if self.map[hash_key]: self.map[hash_key][self.pos(key)] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
