"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None

        p1 = head
        while p1:
            if p1.child:
                self.flatten(p1.child)

                p2 = p1.child
                while p2.next: p2 = p2.next

                n1 = p1
                n2 = p1.child
                n3 = p2
                n4 = p1.next

                p1.child = None

                n1.next = n2
                n2.prev = n1

                if n4:
                    n3.next = n4
                    n4.prev = n3

                p1 = n4
            else:
                p1 = p1.next

        return head
