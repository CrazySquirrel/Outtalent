"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        nodes = [root]
        while nodes:
            tmp = []
            l = len(nodes) - 1
            for i, node in enumerate(nodes):
                if i < l:
                    node.next = nodes[i + 1]
                else:
                    node.next = None
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            nodes = tmp
        return root
