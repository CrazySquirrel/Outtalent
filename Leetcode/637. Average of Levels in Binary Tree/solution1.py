# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        nodes = [root]
        result = []
        while nodes:
            tmp = []
            s = 0
            for node in nodes:
                s += node.val
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            result.append(s / len(nodes))
            nodes = tmp
        return result
