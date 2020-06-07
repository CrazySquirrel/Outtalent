# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def clone(self, node: TreeNode, delta: int) -> TreeNode:
        if not node: return None
        return TreeNode(node.val + delta, left=self.clone(node.left, delta), right=self.clone(node.right, delta))

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0: return []
        dp = [[] for i in range(n + 1)]
        dp[0].append(None)
        for i in range(1, n + 1):
            for j in range(0, i):
                for l in dp[j]:
                    for r in dp[i - j - 1]:
                        dp[i].append(TreeNode(j + 1, left=l, right=self.clone(r, j + 1)))
        return dp[n]
