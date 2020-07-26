# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        result = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            result.append(str(node.val))
            if node.right: nodes.append(node.right)
            if node.left: nodes.append(node.left)
        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        preorder = [int(val) for val in data.split()]
        root = TreeNode(preorder[0])
        s = [root]
        for i in range(1, len(preorder)):
            node = None
            while s and preorder[i] > s[-1].val: node = s.pop()
            if node:
                node.right = TreeNode(preorder[i])
                s.append(node.right)
            else:
                s[-1].left = TreeNode(preorder[i])
                s.append(s[-1].left)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
