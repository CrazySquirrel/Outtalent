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
        return self.pathSumRecursive(root, 0, sum)

    def pathSumRecursive(self, node: TreeNode, acc: int, sum: int) -> int:
        if not node: return 0
        current_acc = acc + node.val
        self.acc_map[current_acc] += 1
        left_sum = self.pathSumRecursive(node.left, current_acc, sum)
        right_sum = self.pathSumRecursive(node.right, current_acc, sum)
        self.acc_map[current_acc] -= 1
        return self.acc_map[current_acc - sum] + left_sum + right_sum
