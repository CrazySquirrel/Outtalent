"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []

        result, stack = [], [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])

        return result
