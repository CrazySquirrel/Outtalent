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
        cur = head
        stack = [cur]
        while stack:
            now = stack.pop(-1)
            if now != head:
                cur.next, now.prev = now, cur
                cur.child = None
                cur = now
            if now.next:
                stack.append(now.next)
            if now.child:
                stack.append(now.child)
        return head
