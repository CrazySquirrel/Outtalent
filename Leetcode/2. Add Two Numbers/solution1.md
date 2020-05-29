# Elementary Math

## Intuition

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.

![](1.svg)

> Figure 1. Visualization of the addition of two numbers: 342+465=807.
> Each node contains a single digit and the digits are stored in reverse order.

## Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1 and l2. Since each digit is in the range of 0…9, summing two digits may "overflow". For example 5+7=12. In this case, we set the current digit to 2 and bring over the carry=1 to the next iteration. carry must be either 0 or 1 because the largest possible sum of two digits (including the carry) is 9+9+1=19.

The pseudocode is as following:

* Initialize current node to dummy head of the returning list.
* Initialize carry to 0.
* Initialize p and q to head of l1 and l2 respectively.
* Loop through lists l1 and l2 until you reach both ends.
    * Set x to node p's value. If p has reached the end of l1, set to 0.
    * Set y to node q's value. If q has reached the end of l2, set to 0.
    * Set sum=x+y+carry.
    * Update carry=sum/10.
    * Create a new node with the digit value of (summod10) and set it to current node's next, then advance current node to next.
    * Advance both p and q.
* Check if carry=1, if so append a new node with digit 1 to the returning list.
* Return dummy head's next node.

Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

Take extra caution of the following cases:

| Test&nbsp;case      | Explanation                                                                   |
|---------------------|-------------------------------------------------------------------------------|
| l1=[0,1] l2=[0,1,2] | When one list is longer than the other.                                       |
| l1=[] l2=[0,1]      | When one list is null, which means an empty list.                             |
| l1=[9,9] l2=[1]     | The sum could have an extra carry of one at the end, which is easy to forget. |

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = curr_head = ListNode()
        p, q = l1, l2

        carry = 0

        while p or q:
            if p:
                carry += p.val
                p = p.next

            if q:
                carry += q.val
                q = q.next

            curr_head.next = ListNode(carry % 10)
            curr_head = curr_head.next
            carry //= 10

        if carry > 0:
            curr_head.next = ListNode(carry)

        return dummy_head.next
```

## Complexity Analysis

* Time complexity: O(max(m,n)).

Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

* Space complexity: O(max(m,n)).

The length of the new list is at most max(m,n)+1.

## Follow up

What if the the digits in the linked list are stored in non-reversed order? For example:

(3→4→2)+(4→6→5)=8→0→7

[Next](solution2.md)