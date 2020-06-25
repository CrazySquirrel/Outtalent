# List comprehension

## Algorithm

* Using list comprehension create new array without val elements

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [n for n in nums if n != val]
        return len(nums)
```

## Complexity analysis

* Time complexity: O(n).

Where k is a cost of pop i element

* Space complexity: O(n).

We need additional space for temporary list

[Prev](solution1.md) [Next](solution3.md)