# Naive approach

## Algorithm

* Concat and sort temporary array
* Return middle element

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_mix = sorted(nums1 + nums2)
        len_nums_mix = len(nums_mix)
        s, b = divmod(len_nums_mix, 2)
        if b == 0:
            return (nums_mix[s - 1] + nums_mix[s]) / 2
        else:
            return nums_mix[s]
```

## Complexity Analysis

* Time complexity: O(n+m+(n*m)log(n*m)). 

* Space complexity: O(n+m). 

[Next](solution2.md)