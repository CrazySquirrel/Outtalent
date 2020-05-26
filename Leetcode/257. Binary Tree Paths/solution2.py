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

        def backtrack(path: List[int], node: TreeNode) -> None:
            path.append(node.val)

            if not node.left and not node.right:
                result.append('->'.join(map(str, path)))

            if node.left:
                backtrack(path, node.left)

            if node.right:
                backtrack(path, node.right)

            path.pop()

        backtrack([], root)

        return result
