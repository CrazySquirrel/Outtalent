# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        nodes = [root]
        result = []
        direction = 1
        while nodes:
            tmp = []
            result.append([])
            for node in nodes:
                result[-1].append(node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            nodes = tmp
            if direction == -1: result[-1] = result[-1][::-1]
            direction *= -1
        return result
