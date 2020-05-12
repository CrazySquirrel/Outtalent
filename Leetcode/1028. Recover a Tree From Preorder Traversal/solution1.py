# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createNode(self, buffer: str, level: int, stack: List[TreeNode]) -> None:
        node = TreeNode(int(buffer))
        if level >= len(stack):
            stack.append(node)
        else:
            stack[level] = node
        if level > 0:
            parent = stack[level - 1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node

    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        level = 0
        buffer = ''

        for c in S:
            if c == '-':
                if buffer and buffer[0] != '-':
                    self.createNode(buffer, level, stack)
                    buffer = c
                else:
                    buffer += c
            else:
                if buffer and buffer[0] == '-':
                    level = len(buffer)
                    buffer = c
                else:
                    buffer += c

        self.createNode(buffer, level, stack)

        return stack[0]
