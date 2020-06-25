# Linear Scan

## Algorithm

* Iterate i from 0 to length of nums:
    * If nums[i] = target then return i
* Return -1

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target: return i
        return -1
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(1)

[Next](solution2.md)