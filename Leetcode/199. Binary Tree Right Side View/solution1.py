# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        nodes = [root]
        result = []
        while nodes:
            result.append(nodes[-1].val)
            tmp = []
            for node in nodes:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            nodes = tmp
        return result
