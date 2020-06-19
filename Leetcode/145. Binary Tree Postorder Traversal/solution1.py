# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        stack = []
        result = []

        while True:
            while root:
                if root.right: stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.right and stack and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                result.append(root.val)
                root = None

            if not stack: break

        return result
