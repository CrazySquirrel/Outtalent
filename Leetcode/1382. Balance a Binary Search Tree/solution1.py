# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, list: List[TreeNode], lo: int, hi: int) -> TreeNode:
        mid = lo + hi >> 1
        node = list[mid]
        node.left = self.build(list, lo, mid) if lo < mid else None
        node.right = self.build(list, mid + 1, hi) if mid + 1 < hi else None
        return node

    def inorder(self, node: TreeNode) -> List[TreeNode]:
        nodes = []
        stack = [node]
        while stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            nodes.append(node)
            node = node.right
        return nodes

    def balanceBST(self, root: TreeNode) -> TreeNode:
        list = self.inorder(root)
        return self.build(list, 0, len(list) - 1)
