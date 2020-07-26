"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(x: int, y: int, l: int) -> 'Node':
            if l == 1:
                node = Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                m = l // 2

                top_left = dfs(x, y, m)
                top_right = dfs(x, y + m, m)
                bottom_left = dfs(x + m, y, m)
                bottom_right = dfs(x + m, y + m, m)

                value = top_left.val or top_right.val or bottom_left.val or bottom_right.val

                if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                    node = Node(value, True, None, None, None, None)
                else:
                    node = Node(value, False, top_left, top_right, bottom_left, bottom_right)

            return node

        return grid and dfs(0, 0, len(grid)) or None
