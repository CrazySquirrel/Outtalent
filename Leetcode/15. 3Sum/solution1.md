# Brute Force

## Algorithm

1. Iterate through nums list using 3 pointers:
    * i - from 0 to length of the list - 2
    * j - from i + 1 to length of the list - 1
    * k - from j + 1 to length of the list
2. If sum of nums[i] + nums[j] + nums[k] equals zero then add it to the results

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add((nums[i], nums[j], nums[k]))
        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>3</sup>)

* Space complexity: O(r)

Where: 
 * n is the length on nums list
 * r is the length or result list
 
 [Next](solution2.md)
 