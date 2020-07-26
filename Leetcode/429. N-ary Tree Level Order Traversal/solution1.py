"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        nodes = [root]
        result = []
        while nodes:
            tmp = []
            result.append([])
            for node in nodes:
                result[-1].append(node.val)
                if node.children: tmp.extend(node.children)
            nodes = tmp
        return result
