# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        level = [root]
        result = []
        while level:
            new_level = []
            val = []
            for node in level:
                val.append(node.val)
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            level = new_level
            result.append(val)
        return result[::-1]
