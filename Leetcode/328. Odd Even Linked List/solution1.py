# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode()
        even = ListNode()

        odd_head = odd
        even_head = even

        i = 1

        while head:
            if i % 2:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next

            head = head.next

            i += 1

        odd.next = even_head.next
        even.next = None

        return odd_head.next
