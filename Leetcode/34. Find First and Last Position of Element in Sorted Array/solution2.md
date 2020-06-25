# Binary Search

## Algorithm

* Search for target or less with binary Search (left = True)
* Search for target or grater with binary Search (left = False) starting from start
* Return [start, end] pair

* Binary search:
    * Set l and r to 0 and length of nums - 1
    * Iterate while l less or equal to r:
        * Set m to l + (r - l) / 2
        * If nums[m] > target or (left and nums[m] == target) set r = m - 1 else l = m + 1
        * Return l

```python
class Solution:
    def bisect(self, nums: List[int], target: int, left: bool) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > target or (left and nums[m] == target):
                r = m - 1
            else:
                l = m + 1

        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.bisect(nums, target, True)

        if start == len(nums) or nums[start] != target: return [-1, -1]

        end = self.bisect(nums, target, False) - 1

        return [start, end]
```

## Complexity Analysis

* Time complexity: O(log(n))

* Space complexity: O(1)

[Prev](solution1.md) [Next](solution3.md)