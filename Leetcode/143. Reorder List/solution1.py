# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return

        ltmp = []
        cur = head

        while cur:  # into a list
            ltmp.append(cur)
            cur = cur.next

        n = len(ltmp)

        for i in range(n // 2):
            ltmp[i].next = ltmp[n - 1 - i]
            ltmp[n - 1 - i].next = ltmp[i + 1]

        ltmp[n // 2].next = None
