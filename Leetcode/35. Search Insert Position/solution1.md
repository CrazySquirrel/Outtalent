# Linear Scan

## Algorithm

* Iterate i from 0 to length of nums:
    * If nums[i] >= target return i
* Return length of nums

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target: return i
        return len(nums)
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(1)

[Next](solution2.md)