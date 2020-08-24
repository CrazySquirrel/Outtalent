# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.recover(self.root, 0)

    def recover(self, root: TreeNode, val: int) -> None:
        root.val = val
        if root.left: self.recover(root.left, 2 * val + 1)
        if root.right: self.recover(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return self.lookup(self.root, target)

    def lookup(self, root: TreeNode, target: int) -> bool:
        if not root: return False
        if root.val > target: return self.lookup(root.left, target)
        if root.val == target: return True
        return self.lookup(root.right, target) or self.lookup(root.left, target)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
