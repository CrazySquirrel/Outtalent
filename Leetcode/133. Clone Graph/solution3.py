"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        if len(node.neighbors) == 0: return Node(node.val)

        seenDict = {}
        stack = [node]
        visited = {}

        while stack:
            currNode = stack.pop(0)

            if currNode in visited: continue

            if currNode not in seenDict:
                newNode = Node(currNode.val)
                seenDict[currNode] = newNode
            else:
                newNode = seenDict[currNode]

            for neighbor in currNode.neighbors:
                if neighbor in seenDict:
                    newNode.neighbors.append(seenDict[neighbor])
                else:
                    temp = Node(neighbor.val)
                    newNode.neighbors.append(temp)
                    seenDict[neighbor] = temp

                stack.append(neighbor)
            visited[currNode] = 1

        return seenDict[node]
