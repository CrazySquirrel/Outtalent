# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []
        node = root
        while node:
            if not node.left:
                result.append(node.val)
                node = node.right
            else:
                tmp = node.left
                while tmp.right: tmp = tmp.right
                tmp.right = node

                tmp = node
                node = node.left
                tmp.left = None
        return result
