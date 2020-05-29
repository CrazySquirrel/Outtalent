# Binary search in range

## Algorithm

1. Sort list of nums
2. Count each numbers in nums list
3. Iterate through unique numbers from nums with pointer i and value itemI:
    * If itemI equal to zero and there are more then 2 zeros in nums then add [0,0,0] to the results
    * If itemI is not equal to zero and are more then 1 itemI in counter and at least one -2 * itemI in counter 
    then add [itemI, itemI, -2 * itemI] to the results
    * If itemI smaller the zero:
        1. Get target as -itemI
        2. Find left index smaller than i + 1 of (target - greatest nums) with binary search left
        3. Find right index smaller than left of (target / 2) with binary search right
        4. Iterate with itemJ through nums from left to right indexes:
            1. Get itemK as target - itemJ
            2. If itemK in counter and itemK not equal to itemJ then add [itemI, itemJ, itemK] to the results
4. Return results
        

```python
from collections import Counter
from bisect import bisect_left, bisect_right


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = sorted(counter)
        result = set()

        for i, itemI in enumerate(nums):
            if itemI == 0:
                if counter[itemI] > 2:
                    result.add((0, 0, 0))
            else:
                if counter[itemI] > 1 and -2 * itemI in counter:
                    result.add((itemI, itemI, -2 * itemI))

            if itemI < 0:
                target = -itemI
                left = bisect_left(nums, target - nums[-1], i + 1)
                right = bisect_right(nums, target // 2, left)

                for itemJ in nums[left: right]:
                    itemK = target - itemJ
                    
                    if itemK in counter and itemK != itemJ:
                        result.add((itemI, itemJ, itemK))

        return result
```

## Complexity Analysis

* Time complexity: O(n + m)

* Space complexity: O(n + r)

Where: 
 * n is the length on nums list
 * m is the range from left ro right index
 * r is the length or result list
 
[Prev](solution5.md)
 