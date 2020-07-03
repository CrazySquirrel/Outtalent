# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, Solution.BOTH_PENDING)]

        one_node_found = False

        LCA_index = -1

        while stack:
            parent_node, parent_state = stack[-1]

            if parent_state != Solution.BOTH_DONE:

                if parent_state == Solution.BOTH_PENDING:

                    if parent_node == p or parent_node == q:

                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1

                    child_node = parent_node.left
                else:
                    child_node = parent_node.right

                stack.pop()
                stack.append((parent_node, parent_state - 1))

                if child_node: stack.append((child_node, Solution.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1

                stack.pop()

        return None
