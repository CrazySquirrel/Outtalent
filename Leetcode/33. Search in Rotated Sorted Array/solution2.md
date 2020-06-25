# Binary Search

## Algorithm

* Set l and h to 0 and length of nums
* Iterate while l less or equal to h:
    * Set m to l + (h - l) / 2
    * If nums[m] = target return m
    * If nums[l] <= nums[m]:
        * If nums[l] <= target < nums[m] set h = m - 1 else set l = m + 1
    * Else:
        * If nums[m] < target <= nums[h] set l = m + 1 else set h = m - 1
* Return -1

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:

            m = l + (h - l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1

        return -1
```

## Complexity Analysis

* Time complexity: O(log(n))

* Space complexity: O(1)

[Prev](solution1.md)