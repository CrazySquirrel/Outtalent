class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__values = {}
        self.__access = []

    def get(self, key: int) -> int:
        if key in self.__values:
            self.__access.remove(key)
            self.__access.append(key)
            return self.__values[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.capacity: return

        if key in self.__values:
            self.__access.remove(key)
        else:
            while len(self.__values) >= self.capacity: self.cleanup()

        self.__access.append(key)
        self.__values[key] = value

    def cleanup(self):
        del self.__values[self.__access.pop(0)]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
