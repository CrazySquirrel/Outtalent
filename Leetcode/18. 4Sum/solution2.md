# Four pointers (Optimized)

## Algorithm

1. Sort nums list
2. Iterate pointer a from 0 to length - 3:
    * If a grater than zero and nums[a] is equal to nums[a - 1] then continue
    * If nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] grater than target then break
    * If nums[a] + nums[n - 3] + nums[n - 2] + nums[n - 1] smaller than target then continue
    1. Iterate pointer b from a + 1 to length -2:
        * If b grater than a + 1 and nums[b] is equal to nums[b - 1] then continue
        * If nums[a] + nums[b] + nums[b + 1] + nums[b + 2] grater than target then break
        * If nums[a] + nums[b] + nums[n - 2] + nums[n - 1] smaller than target then continue
        1. Set pointer c to b + 1 and pointer d to length - 1
        2. Get ram_target as target - (nums[a] + nums[b])
        3. Iterate while c smaller than d:
            * If nums[c] + nums[d] grater than rem_target then decrement d
            * If nums[c] + nums[d] smaller than rem_target then increment c
            * If nums[c] + nums[d] is equal to rem_target then add [nums[a], nums[b], nums[c], nums[d]] to the results and decrement d and increment c
3. Return results

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = set()

        n = len(nums)

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target: break
            if nums[a] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target: break
                if nums[a] + nums[b] + nums[n - 2] + nums[n - 1] < target: continue

                c, d = b + 1, n - 1

                rem_target = target - (nums[a] + nums[b])

                while c < d:
                    if nums[c] + nums[d] > rem_target:
                        d -= 1
                    elif nums[c] + nums[d] < rem_target:
                        c += 1
                    else:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1

        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>3</sup>)<sup>*</sup>

<sup>*</sup> - it's n<sup>3</sup> but due to additional checks it's much faster

* Space complexity: O(1)

[Prev](solution1.md)
