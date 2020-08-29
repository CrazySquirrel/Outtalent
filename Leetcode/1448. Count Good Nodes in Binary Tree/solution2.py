# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def count(node: TreeNode, parent: int) -> int:
            result = 0

            if node.val >= parent:
                result += 1
                parent = node.val

            if node.left:
                result += count(node.left, parent)

            if node.right:
                result += count(node.right, parent)

            return result

        return count(root, root.val)
