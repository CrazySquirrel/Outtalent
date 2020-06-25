# Binary Search

## Algorithm

* Create index l and r and set them to 0 and length of nums - 1
* Iterate while l less or equal to r:
    * Set m = l + (r - l) // 2
    * If nums[m] > target then set r to m - 1
    * If nums[m] < target then set l = m + 1
    * If nums[m] = target then return m
* Return l

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l
```

## Complexity Analysis

* Time complexity: O(len(n))

* Space complexity: O(1)

[Prev](solution1.md) [Next](solution3.md)