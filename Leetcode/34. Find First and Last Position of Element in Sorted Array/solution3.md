# Binary Search

## Algorithm

* Do the same as in [approach 2](solution2.md) but with bisect_left, bisect_right
* Set start to bisect_left(nums, target)
* If start grater than length of nums or nums[start] != target then return [-1, -1]
* Set end to bisect_right(nums, target) - 1
* Return [start, end]

```python
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)

        if start == len(nums) or nums[start] != target: return [-1, -1]

        end = bisect_right(nums, target) - 1

        return [start, end]
```

## Complexity Analysis

* Time complexity: O(log(n))

* Space complexity: O(1)

[Prev](solution2.md)