# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index_map = {v: i for i, v in enumerate(inorder)}

        def buildT(start, end):
            if start > end: return None
            v = preorder.pop(0)
            return TreeNode(v, left=buildT(start, index_map[v] - 1), right=buildT(index_map[v] + 1, end))

        return buildT(0, len(inorder) - 1)
