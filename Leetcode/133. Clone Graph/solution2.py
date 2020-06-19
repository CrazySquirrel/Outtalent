"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(current, d):
            if current is None: return None
            if current.val not in d: d[current.val] = Node(current.val)
            node = d[current.val]
            for n in current.neighbors:
                if n.val not in d: helper(n, d)
                node.neighbors.append(d[n.val])
            return node

        return helper(node, {})
