# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        s = [root]
        for i in range(1, len(preorder)):
            node = None
            while s and preorder[i] > s[-1].val: node = s.pop()
            if node:
                node.right = TreeNode(preorder[i])
                s.append(node.right)
            else:
                s[-1].left = TreeNode(preorder[i])
                s.append(s[-1].left)
        return root
