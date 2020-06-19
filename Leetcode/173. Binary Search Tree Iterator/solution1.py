# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.pointer = self.gen(root)
        self.tmp = None

    def gen(self, root: TreeNode):
        if root.left: yield from self.gen(root.left)
        yield root.val
        if root.right: yield from self.gen(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.tmp is not None:
            result = self.tmp
            self.tmp = None
            return result

        return self.pointer.__next__()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        try:
            if self.tmp is None: self.tmp = self.pointer.__next__()
            return self.tmp is not None
        except:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
