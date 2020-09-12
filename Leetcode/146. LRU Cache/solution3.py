class DLinkedNode():
    def __init__(self, key: int = None, value: int = None, prev: 'DLinkedList' = None, next: 'DLinkedList' = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DLinkedList():
    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def pop_tail(self) -> 'DLinkedList':
        res = self.tail.prev
        self.remove_node(res)
        return res

    def move_to_head(self, node: 'DLinkedList') -> None:
        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node: 'DLinkedList') -> None:
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def add_node(self, node: 'DLinkedList') -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


class LRUCache():
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.list = DLinkedList()

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node: return -1
        self.list.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            node = DLinkedNode(key=key, value=value)
            self.cache[key] = node
            self.list.add_node(node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.list.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.list.move_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
