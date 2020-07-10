from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.rank = defaultdict(OrderedDict)
        self.key_to_rank = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_rank: return -1
        return self.rank[self.update(key) + 1][key]

    def update(self, key: int, val: int = None) -> int:
        rank = self.key_to_rank[key]
        self.key_to_rank[key] = rank + 1
        self.rank[rank + 1][key] = self.rank[rank][key] if val is None else val
        del self.rank[rank][key]
        return rank

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_to_rank: return self.update(key, value)

        if len(self.key_to_rank) == self.capacity:
            for i in range(len(self.rank)):
                if len(self.rank[i]) > 0: break
            k, _ = self.rank[i].popitem(last=False)
            del self.key_to_rank[k]

        self.key_to_rank[key] = 0
        self.rank[0][key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
