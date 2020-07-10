# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next: return head

        odd = head
        even_head = even = odd.next

        while even and even.next:
            odd.next = even.next
            odd = even.next

            even.next = odd.next
            even = odd.next

        odd.next = even_head

        return head
