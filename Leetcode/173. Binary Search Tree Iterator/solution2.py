# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = []
        self.curnode = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.curnode

        while n:
            self.data.append(n)
            n = n.left

        n1 = self.data.pop()
        self.curnode = n1.right

        return n1.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curnode or len(self.data) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
