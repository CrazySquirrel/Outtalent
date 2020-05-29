# Two sum

## Algorithm

1. Create dictionary two_sum and set three_sum
2. Use i pointer to iterate through nums:
    1. Check if there is -nums[i] key in two_sum dictionary. 
        * If there is then iterate through values from two_sum[-nums[i]]
        * Sort tmp list of [value + nums[i]] and add it to three_sum
    2. Iterate pointer j from 0 to i-1:
        * Get sum s of nums[i], nums[j]
        * Create dictionary with key s in two_sum
        * Add keys i j to the dictionary two_sum[s]
3. Return values of three_sum

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = {}
        three_sum = {}

        for i in range(len(nums)):
            for value in two_sum.get(-nums[i], {}).values():
                tmp = sorted(value + [nums[i]])
                three_sum["%d,%d,%d" % (tmp[0], tmp[1], tmp[2])] = tmp

            for j in range(i):
                add_value = nums[i] + nums[j]
                two_sum[add_value] = two_sum.get(add_value, {})
                key = (nums[j], nums[i]) if nums[j] < nums[i] else (nums[i], nums[j])
                two_sum[add_value]["%d,%d" % key] = [nums[j], nums[i]]

        return [v for k, v in three_sum.items()]
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup> + n * m)

* Space complexity: O(n<sup>2</sup>)

Where: 
 * n is the length on nums list
 * r is the length or result list
 * m is the length of largest two sum dictionary
 
 [Prev](solution2.md) [Next](solution4.md)
 