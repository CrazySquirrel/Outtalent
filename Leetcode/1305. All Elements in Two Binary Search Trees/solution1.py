# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
        stack = []
        result = []

        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                result.append(root.val)
                root = root.right
            else:
                break

        return result

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.inorder(root1)
        list2 = self.inorder(root2)

        return sorted(list1 + list2)
