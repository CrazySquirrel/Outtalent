# Pop elements

## Algorithm

* Iterate while i less then length of nums:
* If nums[i] = val then pop nums[i] else increment i
* Return i

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val: nums.pop(i)
            else: i += 1
        return len(nums)
```

## Complexity analysis

* Time complexity: O(n<sup>2</sup>).

Where k is a cost of pop i element

* Space complexity: O(1).

[Next](solution2.md)
