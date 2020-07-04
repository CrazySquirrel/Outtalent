# Brute force

## Algorithm

* Initialize ans=0
* Iterate the array from left to right:
    * Initialize left_max=0 and right_max=0
    * Iterate from the current element to the beginning of array updating:
        * left_max=max(left_max,height[j])
    * Iterate from the current element to the end of array updating:
        * right_max=max(right_max,height[j])
    * Add min(left_max,right_max)−height[i] to ans

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        result = 0

        for i in range(1, len(height) - 1):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            result += min(left_max, right_max) - height[i]

        return result
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>)

* Space complexity: O(1)

[Next](solution2.md)