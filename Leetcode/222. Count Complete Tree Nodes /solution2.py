# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def getDepthLeft(node: TreeNode) -> int:
            result = 0
            while node:
                result += 1
                node = node.left
            return result

        def getDepthRight(node: TreeNode) -> int:
            result = 0
            while node:
                result += 1
                node = node.right
            return result

        def getLastLevelLength(node: TreeNode, depth: int) -> int:
            result = 0
            for i in range(depth - 1):
                left = getDepthRight(node.left)
                if left < depth - i - 1:
                    node = node.left
                    result += 0
                else:
                    node = node.right
                    result += 2 ** (depth - i - 2)
            return result

        depthLeft = getDepthLeft(root)
        depthRight = getDepthRight(root)

        if depthLeft == depthRight:
            return 2 ** depthLeft - 1

        return 2 ** (depthLeft - 1) - 1 + getLastLevelLength(root, depthLeft)
