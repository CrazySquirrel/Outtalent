# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root

    def find(self, target: int) -> bool:
        if target < 0: return False
        if target == 0: return self.root is not None

        path = []

        while target > 0:
            path.insert(0, target)

            if target % 2 == 1:
                target = (target - 1) // 2
            else:
                target = (target - 2) // 2

        tmp = self.root

        for p in path:
            if p % 2 == 1:
                tmp = tmp.left
            else:
                tmp = tmp.right

            if not tmp: return False

        return True

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
