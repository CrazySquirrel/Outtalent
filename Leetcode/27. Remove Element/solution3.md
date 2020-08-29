# Two Pointers

## Algorithm

* Create index i = 0
* Iterate j from 0 to length nums:
    * if nums[j] not equal to val set nums[i] = nums[j] and increment i
* Return i

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        nums[:] = nums[:i]
        return i
```

## Complexity analysis

* Time complexity: O(n).

* Space complexity: O(1).

[Prev](solution2.md) [Next](solution4.md)