"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        if node.val in self.visited: return self.visited[node.val]
        self.visited[node.val] = Node(node.val)
        if node.neighbors:
            self.visited[node.val].neighbors = []
            for neighbor in node.neighbors:
                self.visited[node.val].neighbors.append(self.cloneGraph(neighbor))
        return self.visited[node.val]
