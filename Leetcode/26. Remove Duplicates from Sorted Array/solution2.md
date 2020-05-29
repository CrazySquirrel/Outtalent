# One Pointer

## Algorithm

1. Create pointer i
2. Iterate through list and if nums[i-1] equal to nums[i] then remove nums[i] otherwise move pointer i by 1
3. Return the length of the new array

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]: nums.pop(i)
            else: i += 1
        return len(nums)
```

* Time complextiy: O(n).

* Space complexity: O(1).

[Prev](solution1.md) [Next](solution3.md)