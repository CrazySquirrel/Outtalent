# Two pointers

## Algorithm

1. Sort list on nums
2. Iterate i pointer from 0 to length - 2:
    1. Create j pointer equal to i + 1 and k pointer equal to length - 1
    2. Iterate while i < k:
        1. Get sum of nums[i] + nums[j] + nums[k]:
            * if sum equal to zero then add nums[i], nums[j], nums[k] to the result
            * if sum smaller or equal to zero then increment i
            * if sum greater than zero decrement then k 
3. Return results

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = set()
        nums.sort()
        for i in range(0, length - 2):
            j = i + 1
            k = length - 1
            while j < k:
                sum0 = nums[i] + nums[j] + nums[k]
                if sum0 == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif sum0 < 0:
                    j += 1
                elif sum0 > 0:
                    k -= 1
        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>)

* Space complexity: O(r)

Where: 
 * n is the length on nums list
 * r is the length or result list

[Prev](solution3.md) [Next](solution5.md)