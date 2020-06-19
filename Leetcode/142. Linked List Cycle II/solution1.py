# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        visited = set()
        while head:
            if head in visited: return head
            visited.add(head)
            head = head.next
        return None
