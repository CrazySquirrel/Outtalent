# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map_inorder = {v: i for i, v in enumerate(inorder)}

        def recur(start, end):
            if start > end: return None
            v = postorder.pop()
            return TreeNode(v, right=recur(map_inorder[v] + 1, end), left=recur(start, map_inorder[v] - 1))

        return recur(0, len(inorder) - 1)
