# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root: TreeNode, num: int) -> TreeNode:
        if not root: return TreeNode(num)

        if root.val > num:
            root.left = self.insert(root.left, num)
        else:
            root.right = self.insert(root.right, num)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])

        for i in range(1, len(preorder)):
            root = self.insert(root, preorder[i])

        return root
