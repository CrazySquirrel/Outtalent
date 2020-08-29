# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node: TreeNode):
            nonlocal result, path

            if not path or node.val >= path[-1]:
                path.append(node.val)
                result += 1
            else:
                path.append(path[-1])

            if node.left: count(node.left)
            if node.right: count(node.right)

            path.pop()

        path = []
        result = 0

        if root: count(root)

        return result
