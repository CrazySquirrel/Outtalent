# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return None

        summ = 0
        stack = []
        current = root

        while True:
            if current:
                stack.append(current)
                current = current.right
            elif stack:
                current = stack.pop()
                summ += current.val
                current.val = summ
                current = current.left
            else:
                break

        return root
