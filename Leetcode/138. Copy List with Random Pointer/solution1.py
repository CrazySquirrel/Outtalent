"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None
        if head in self.visited: return self.visited[head]

        copy = Node(head.val)

        self.visited[head] = copy

        copy.next = self.copyRandomList(head.next)
        copy.random = self.copyRandomList(head.random)

        return copy
