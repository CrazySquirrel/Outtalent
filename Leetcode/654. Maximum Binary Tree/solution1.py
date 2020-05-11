# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        i = nums.index(max(nums))

        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i + 1:])

        return root
