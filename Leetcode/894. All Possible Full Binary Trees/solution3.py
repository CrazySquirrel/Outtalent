# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0: return []
        dp = [[] for i in range(N + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, N + 1, 2):
            for j in range(1, i, 2):
                k = i - j - 1
                for l in dp[j]:
                    for r in dp[k]:
                        root = TreeNode(0, left=l, right=r)
                        dp[i].append(root)
        return dp[N]
