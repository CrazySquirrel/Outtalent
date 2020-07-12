# Two sum

## Algorithm

1. Create two_sum dictionary
2. Iterate with pointer a from 0 to length - 1 and pointer b from a + 1 to length:
    1. Get sum_ab ab as nums[a] + nums[b]
    2. Add to two_sum[sum_ab] indexes a and b
3. Iterate though two_sum dictionary:
    1. Get sum_cd as target - sum_ab
    2. If sum_cd is not in two_sum dictionary then continue
    3. Iterate with pointers a, b and c, d though two_sum[sum_ab] and two_sum[sum_cd]:
        1. If a ≠ b ≠ c ≠ d add [nums[a], nums[b], nums[c], nums[d]] to the results
4. Return results

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        two_sum = collections.defaultdict(list)

        for a in range(len(nums) - 1):
            for b in range(a + 1, len(nums)):
                two_sum[nums[a] + nums[b]].append((a, b))

        result = set()

        for sum_ab in two_sum:
            sum_cd = target - sum_ab

            if sum_cd not in two_sum: continue

            for a, b in two_sum[sum_ab]:
                for c, d in two_sum[sum_cd]:
                    if a != c and a != d and b != c and b != d:
                        result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))

        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>3</sup>)

* Space complexity: O(n<sup>2</sup>)

[Next](solution2.md)