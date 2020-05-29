# Binary search

1. Sort the list of nums
2. Iterate through nums list using 3 pointers:
    * i - from 0 to length of the list - 2
    * j - from i + 1 to length of the list - 1
3. For each pair of i and j try to find index k greater then j such that nums[k] = 0 - nums[i] - nums[j] in the list using binary search
4. If key exist add i j k to the results

```python
from bisect import bisect_left


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                x = 0 - nums[i] - nums[j]
                k = bisect_left(nums, x, lo=j + 1)
                if k != len(nums) and nums[k] == x:
                    result.add((nums[i], nums[j], nums[k]))

        return result
```

## Complexity Analysis

* Time complexity: O(n*log(n) + n<sup>2</sup>*log(n)) -> O(n<sup>2</sup>*log(n))

We need n*log(n) to sort nums list and n<sup>2</sup>*log(n) to iterate through list with i and j and search for k

* Space complexity: O(r)

Where: 
 * n is the length on nums list
 * r is the length or result list
 
 [Prev](solution1.md) [Next](solution3.md)
 