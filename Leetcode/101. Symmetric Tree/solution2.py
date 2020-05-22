# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root, root]
        while q:
            node1 = q.pop()
            node2 = q.pop()

            if not node1 and not node2: continue
            if not node1 or not node2: return False
            if node1.val != node2.val: return False

            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)

        return True
