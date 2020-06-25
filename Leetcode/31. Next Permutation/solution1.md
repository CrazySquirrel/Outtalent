# Single Pass Approach

## Algorithm

* Find first decreasing element from left to right and save it index to i
* Find element that just larger nums[i] and save it index to j
* Swap nums[i] and nums[j]
* Reverse nums from i+1 to the end of nums

![](1.gif)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        while i > -1 and nums[i] >= nums[i + 1]: i -= 1

        if i > -1:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]: j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]

        nums[i + 1:] = nums[i + 1:][::-1]
```

## Complexity Analysis

* Time complexity: O(n)

In worst case, only two scans of the whole array are needed.

* Space complexity: O(1)

No extra space is used. In place replacements are done.