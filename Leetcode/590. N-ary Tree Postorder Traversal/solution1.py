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

        result = []
        for child in root.children:
            result.extend(self.postorder(child))
        result.append(root.val)

        return result
