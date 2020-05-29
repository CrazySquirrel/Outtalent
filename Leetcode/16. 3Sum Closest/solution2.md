# Two pointers (Optimized)

Use a similar [approach1](solution1.md)

## Algorithm

1. Sort list on nums
2. Iterate i pointer from 0 to length - 2:
    1.
        * Set r index to length-1
        * Get rs as sum of num + nums[r] + nums[r - 1]
        * If rs smaller than target then update result with rs <sup>*</sup> and continue
    2.
        * Set l index to i + 1
        * Get ls as sum of num + nums[l] + nums[l + 1]
        * If ls grater than target then update result with ls <sup>*</sup> and continue
        
    3. Iterate while i < k:
        * Get sum of nums[i] + nums[j] + nums[k]
        * Update result with sum <sup>*</sup>
        * if sum smaller or equal to zero then increment i
        * if sum greater than zero decrement then k 
3. Return result

<sup>*</sup> - Update result with new sum if diff between old result and target is greater than diff between new sum and target

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return sum(nums)
        nums.sort()
        length = len(nums)
        result = inf

        for i, num in enumerate(nums[0:-2]):
            r = length - 1
            rs = num + nums[r] + nums[r - 1]

            if rs < target:
                result = min(result, rs, key=lambda x: abs(x - target))
                continue

            l = i + 1
            ls = num + nums[l] + nums[l + 1]

            if ls > target:
                result = min(result, ls, key=lambda x: abs(x - target))
                continue

            while l < r:
                s = num + nums[l] + nums[r]

                result = min(result, s, key=lambda x: abs(x - target))

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target

        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>)<sup>*</sup>

<sup>*</sup> - it'll be smaller then just O(n<sup>2</sup>) because of rs and ls cases

* Space complexity: O(1)

[Prev](solution1.md)