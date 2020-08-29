# Two Pointers (rare)

## Algorithm

* Create index i = 0
* Save nums length to n
* Iterate while i less than n:
    * If nums[i] = val then nums[i] = nums[n - 1] and decrement n else inclement i
* Return n

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        nums[:] = nums[:n]
        return n
```

## Complexity analysis

* Time complexity: O(n).

* Space complexity: O(1).

[Prev](solution3.md)