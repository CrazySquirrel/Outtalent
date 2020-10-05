"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        result = 0
        nodes = [root]
        while nodes:
            tmp = []
            for node in nodes: tmp.extend(node.children)
            nodes = tmp
            result += 1
        return result
