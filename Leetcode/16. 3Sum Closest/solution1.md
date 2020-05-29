# Two pointers

Use a similar approach as in [3Sum approach 4](../15.%203Sum/solution4.md)

# Algorithm

1. Sort list on nums
2. Iterate i pointer from 0 to length - 2:
    1. Create j pointer equal to i + 1 and k pointer equal to length - 1
    2. Iterate while i < k:
        1. Get sum of nums[i] + nums[j] + nums[k]:
            * Get diff between sum and target:
                * If new diff is smaller than previous one then update diff and save new sum to the result
            * if sum equal to target then return result
            * if sum smaller or equal to zero then increment i
            * if sum greater than zero decrement then k 
3. Return result

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return sum(nums)
        length = len(nums)
        result = diff = inf
        nums.sort()
        for i in range(0, length - 2):
            j = i + 1
            k = length - 1
            while j < k:
                sum0 = nums[i] + nums[j] + nums[k]
                if diff > abs(sum0 - target):
                    diff, result = abs(sum0 - target), sum0
                if sum0 == target:
                    return result
                elif sum0 < target:
                    j += 1
                elif sum0 > target:
                    k -= 1
        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>)

* Space complexity: O(1)

[Next](solution2.md)