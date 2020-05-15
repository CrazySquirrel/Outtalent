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

    def merge(self, list1: List[int], list2: List[int]) -> List[int]:
        size_1, size_2 = len(list1), len(list2)

        i, j, res = 0, 0, []

        while i < size_1 and j < size_2:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        return res + list1[i:] + list2[j:]

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return self.merge(self.inorder(root1), self.inorder(root2))
