# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        nodes = [root]
        result = []
        while nodes:
            tmp = []
            result.append([])
            for node in nodes:
                result[-1].append(node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            nodes = tmp
        return result
