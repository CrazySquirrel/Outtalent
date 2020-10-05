# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        node = root
        nodes = []
        result = []
        counter = most_counter = 0
        prev = None
        while True:
            if node is not None:
                nodes.append(node)
                node = node.left
            elif nodes:
                node = nodes.pop()
                if prev == node.val:
                    counter += 1
                else:
                    counter = 1
                if counter > most_counter:
                    most_counter = counter
                    result = []
                if counter == most_counter:
                    result.append(node.val)
                prev = node.val
                node = node.right
            else:
                break
        return result
