from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.acc_map = defaultdict(int)
        self.acc_map[0] = 1

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        return self.pathSumRecursive(root, 0, sum)

    def pathSumRecursive(self, node: TreeNode, acc: int, sum: int) -> int:
        acc += node.val
        self.acc_map[acc] += 1
        left_sum = self.pathSumRecursive(node.left, acc, sum) if node.left else 0
        right_sum = self.pathSumRecursive(node.right, acc, sum) if node.right else 0
        self.acc_map[acc] -= 1
        return self.acc_map[acc - sum] + left_sum + right_sum
