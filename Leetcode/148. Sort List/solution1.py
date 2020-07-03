# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        pre, slow, fast = head, head, head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        dummy = head = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        head.next = l1 if l1 else l2

        return dummy.next
