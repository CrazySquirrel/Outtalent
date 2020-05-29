# Brute Force

## Algorithm

In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>). 

Calculating area for all n(n-1)/2 height pairs.

* Space complexity: O(1).

Constant extra space is used.

[Next](solution2.md)