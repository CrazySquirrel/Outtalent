# Approach 2

## Algorithm

* Iterate i from zero to length of nums
    * Get k index as nums[i] - 1
    * If k index is valid and nums[i] != nums[k] then swap then otherwise increment i
* Iterate i from 0 to n:
    * If nums[i] != i + 1 then return i + 1
* Return n + 1

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1

        n, i = len(nums), 0

        while i < n:
            k = nums[i] - 1

            if 0 <= k < n and nums[i] != nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
            else:
                i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(1)

[Prev](solution1.md)