"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []

        result, q = [], [root]

        while q:
            node = q.pop()
            result.append(node.val)
            q.extend(node.children)

        return result[::-1]
