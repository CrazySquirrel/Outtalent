# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: TreeNode):
        stack = []

        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                yield root.val
                root = root.right
            else:
                break

        yield None

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        pointer1 = self.inorder(root1)
        pointer2 = self.inorder(root2)

        result = []
        v1 = next(pointer1)
        v2 = next(pointer2)

        while v1 != None or v2 != None:
            if v1 != None and v2 != None:
                if v1 > v2:
                    result.append(v2)
                    v2 = next(pointer2)
                else:
                    result.append(v1)
                    v1 = next(pointer1)

            elif v1 != None:
                result.append(v1)
                v1 = next(pointer1)
            else:
                result.append(v2)
                v2 = next(pointer2)

        return result
