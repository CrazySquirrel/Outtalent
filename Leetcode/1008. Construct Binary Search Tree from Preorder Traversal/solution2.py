# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            child = TreeNode(preorder[i])
            parent = root
            while True:
                if parent.val > child.val:
                    if parent.left == None:
                        parent.left = child
                        break
                    parent = parent.left
                else:
                    if parent.right == None:
                        parent.right = child
                        break
                    parent = parent.right
        return root
