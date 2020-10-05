# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node: TreeNode, reverse: bool):
        if reverse:
            if node.right: yield from self.inorder(node.right, reverse)
            yield node
            if node.left: yield from self.inorder(node.left, reverse)
        else:
            if node.left: yield from self.inorder(node.left, reverse)
            yield node
            if node.right: yield from self.inorder(node.right, reverse)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False

        li = self.inorder(root, False)
        ri = self.inorder(root, True)

        lv = li.__next__()
        rv = ri.__next__()

        while rv != lv:
            s = lv.val + rv.val
            if s > k:
                rv = ri.__next__()
            elif s < k:
                lv = li.__next__()
            else:
                return True

        return False
