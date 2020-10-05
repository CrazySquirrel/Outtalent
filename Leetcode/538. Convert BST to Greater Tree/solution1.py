# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def get_successor(node):
            succ = node.right
            while succ.left and succ.left is not node: succ = succ.left
            return succ

        total = 0
        node = root

        while node is not None:
            if node.right:
                succ = get_successor(node)

                if succ.left:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
                else:
                    succ.left = node
                    node = node.right
            else:
                total += node.val
                node.val = total
                node = node.left

        return root
