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
        result = []

        def preOrder(root):
            if not root: return None
            result.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)

        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = [int(val) for val in data.split()]

        def build(minVal: int, maxVal: int) -> TreeNode:
            if vals and minVal < vals[0] < maxVal:
                val = vals.pop(0)
                return TreeNode(val, left=build(minVal, val), right=build(val, maxVal))

        return build(-inf, inf)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
