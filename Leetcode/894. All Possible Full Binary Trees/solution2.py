# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cache = {}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        if N in self.cache: return self.cache[N]
        result = []
        for i in range(1, N, 2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N - i - 1):
                    result.append(TreeNode(0, left=l, right=r))
        self.cache[N] = result
        return self.cache[N]
