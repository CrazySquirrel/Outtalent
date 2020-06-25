# Linear Scan

## Algorithm

* Set start and end index to -1
* Iterate from 0 to length of nums:
    * If nums[i] = target:
        * If start = -1 set start and end to i else set end to i
* Return [start, end] pair

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = end = i
                else:
                    end = i
        return [start, end]
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(1)

[Next](solution2.md)