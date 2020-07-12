# Two Pointers (Hash Set)

## Algorithm

twoSum implementation here is almost the same as in [Two Sum: One-pass Hash Table](solution3.md). 
The only difference is the check to avoid duplicates. Since the array is sorted, we can just compare the found pair with the last one in the result res.

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
        s = set()
        for i in range(len(nums)):
            if (not res or res[-1][1] != nums[i]) and target - nums[i] in s:
                res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res
```

## Complexity Analysis

* Time complexity: O(n<sup>k−1</sup>), or O(n<sup>3</sup>) for 4Sum. 

We have k−2 loops, and twoSum is O(n).
Note that for k>2, sorting the array does not change the overall time complexity.

* Space complexity: O(n)

[Prev](solution3.md)