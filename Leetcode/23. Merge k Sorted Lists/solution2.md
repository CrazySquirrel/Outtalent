# Compare one by one

## Algorithm

* Compare every k nodes (head of every linked list) and get the node with the smallest value.
* Extend the final sorted linked list with the selected nodes.

![](1.png)

![](2.png)

![](3.png)

![](4.png)

![](5.png)

![](6.png)

![](7.png)

![](8.png)

![](9.png)

![](10.png)

![](11.png)

## Complexity Analysis

* Time complexity: O(kN) where k is the number of linked lists.

    * Almost every selection of node in final linked costs O(k) (k-1 times comparison).
    * There are N nodes in the final linked list.

* Space complexity:

    * O(n) Creating a new linked list costs O(n) space.
    * O(1) It's not hard to apply in-place method - connect selected nodes instead of creating new nodes to fill the new linked list.

[Prev](solution1.md) [Next](solution3.md)