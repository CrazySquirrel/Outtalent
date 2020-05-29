# One-pass Hash Table (Optimized)

We going to use the same solution as for [One-pass Hash Table](solution3.md) by with some coding optimizations.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, num in enumerate(nums):
            if num in h: return [h[num], index]
            h[target - num] = index
        return None
```

[Prev](solution3.md)