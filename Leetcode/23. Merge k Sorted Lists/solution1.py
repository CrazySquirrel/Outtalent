# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []

        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next

        dummy = curr = ListNode(0)

        for num in sorted(nums):
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
