# Approach 1

## Algorithm

* Segregate positive numbers from others i.e., move all non-positive numbers to left side
* Traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of value at index x to negative
* Traverse the array again and return the first index which has positive value.
* If there is no positive value in the array then return the length of positive segment + 1

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1

        n = len(nums)

        j = 0
        for i in range(n):
            if nums[i] <= 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        nums = nums[j:]
        n -= j

        for i in range(n):
            k = abs(nums[i]) - 1
            if k < n and nums[k] > 0: nums[k] = -nums[k]

        for i in range(n):
            if nums[i] > 0: return i + 1

        return n + 1
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(1)

[Next](solution2.md)