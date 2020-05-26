a# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []

        result = []

        def backtrack(s: str, node: TreeNode) -> None:
            if not node.left and not node.right:
                result.append(s)

            if node.left:
                backtrack(s + '->' + str(node.left.val), node.left)

            if node.right:
                backtrack(s + '->' + str(node.right.val), node.right)


        backtrack(str(root.val), root)

        return result