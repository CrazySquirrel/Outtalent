# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []

        result = []

        if root.left or root.right:
            for path in self.binaryTreePaths(root.left):
                result.append(str(root.val) + "->" + path)

            for path in self.binaryTreePaths(root.right):
                result.append(str(root.val) + "->" + path)

            return result
        else:
            return [str(root.val)]
