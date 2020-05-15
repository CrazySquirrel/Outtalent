# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: return None
        if not t1: return t2
        if not t2: return t1

        nodes1 = [t1]
        nodes2 = [t2]

        while nodes1 and nodes2:
            node1 = nodes1.pop()
            node2 = nodes2.pop()

            node1.val += node2.val

            if node1.left and node2.left:
                nodes1.append(node1.left)
                nodes2.append(node2.left)
            elif node2.left:
                node1.left = node2.left

            if node1.right and node2.right:
                nodes1.append(node1.right)
                nodes2.append(node2.right)
            elif node2.right:
                node1.right = node2.right

        return t1
