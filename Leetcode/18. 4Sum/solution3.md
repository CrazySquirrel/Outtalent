# Two Pointers

## Algorithm

We can implement k - 2 loops using a recursion. We will pass the starting point and k as the parameters. When k == 2, we will call twoSum, terminating the recursion.

* For the main function:
    * Sort the input array nums.
    * Call kSum with start = 0, k = 4, and target, and return the result.

* For kSum function:
    * Check if the sum of k smallest values is greater than target, or the sum of k largest values is smaller than target. Since the array is sorted, the smallest value is nums[start], and largest - the last element in nums.
        * If so, no need to continue - there are no k elements that sum to target.
    * If k equals 2, call twoSum and return the result.
    * Iterate i through the array from start:
        * If the current value is the same as the one before, skip it.
        * Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
        * For each returned set of values:
            * Include the current value nums[i] into set.
            * Add set to the result res.
    * Return the result res.

* For twoSum function:
    * Set the low pointer lo to start, and high pointer hi to the last index.
    * While low pointer is smaller than high:
        * If the sum of nums[lo] and nums[hi] is less than target, increment lo.
            * Also increment lo if the value is the same as for lo - 1.
        * If the sum is greater than target, decrement hi.
            * Also decrement hi if the value is the same as for hi + 1.
        * Otherwise, we found a pair:
            * Add it to the result res.
            * Decrement hi and increment lo.
    * Return the result res.

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(sorted(nums), target, 4)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        if not nums or nums[0] * k > target or target > nums[-1] * k: return []
        if k == 2: return self.twoSum(nums, target)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for sub_sum in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                res.append([nums[i]] + sub_sum)
        return res

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l = len(nums) - 1
        lo, hi = 0, l
        while lo < hi:
            if lo > 0 and nums[lo] == nums[lo - 1]:
                lo += 1
            elif hi < l and nums[hi] == nums[hi + 1]:
                hi -= 1
            else:
                s = nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
        return res
```

## Complexity Analysis

* Time complexity: O(n<sup>k−1</sup>), or O(n<sup>3</sup>) for 4Sum. 

We have k−2 loops, and twoSum is O(n).
Note that for k>2, sorting the array does not change the overall time complexity.

* Space complexity: O(n)

We need O(k) space for the recursion. k can be the same as n in the worst case for the generalized algorithm.
Note that, for the purpose of complexity analysis, we ignore the memory required for the output.

[Prev](solution2.md) [Next](solution4.md)