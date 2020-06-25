# Binary Search

## Algorithm

* Do the same as in [approach 2](solution2.md) but with bisect_left
* Just return bisect_left(nums, target)

```python
from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```

## Complexity Analysis

* Time complexity: O(len(n))

* Space complexity: O(1)

[Prev](solution2.md)