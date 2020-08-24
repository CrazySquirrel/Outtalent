# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.lookup = set()
        self.recover(root, 0)

    def recover(self, root: TreeNode, val: int) -> None:
        self.lookup.add(val)
        if root.left: self.recover(root.left, 2 * val + 1)
        if root.right: self.recover(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.lookup

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
