# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.length = 0

        tmp = head

        while tmp:
            tmp = tmp.next
            self.length += 1

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        tmp = self.head
        for i in range(random.randint(0, self.length - 1)): tmp = tmp.next
        return tmp.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
