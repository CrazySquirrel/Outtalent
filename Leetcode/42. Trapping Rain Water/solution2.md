# Dynamic Programming

## Algorithm

* Find maximum height of bar from the left end up to an index i in the array left_max.
* Find maximum height of bar from the right end up to an index i in the array right_max.
* Iterate over the height array and update ans:
    * Add min(left_max[i],right_max[i])−height[i] to ans

![](1.png)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)

        left_max = [-inf] * n
        left_max[0] = height[0]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max = [-inf] * n
        right_max[-1] = height[-1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        result = 0

        for i in range(1, n - 1):
            result += min(left_max[i], right_max[i]) - height[i]

        return result
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(n)

[Prev](solution1.md) [Next](solution3.md)