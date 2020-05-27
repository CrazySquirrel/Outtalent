# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode("*")
        result.next = head
        prev = result

        while prev.next and prev.next.next:
            curr = prev.next
            next = curr.next

            curr.next = next.next
            next.next = curr

            prev.next = next
            prev = curr

        return result.next
