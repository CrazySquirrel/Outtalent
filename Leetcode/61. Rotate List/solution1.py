# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head

        iterations = 1
        node = head

        while node.next:
            node = node.next
            iterations += 1

        k = k % iterations

        if k == 0: return head

        slow = fast = head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next

        slow.next = None
        fast.next = head

        return temp
