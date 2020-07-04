# Using 2 pointers

## Algorithm

* Initialize left pointer to 0 and right pointer to size-1
* While left<right, do:
    * If height[left] is smaller than height[right]
        * If height[left]≥left_max, update left_max
        * Else add left_max−height[left] to ans
        * Add 1 to left.
    * Else
        * If height[right]≥right_max, update right_max
        * Else add right_max−height[right] to ans
        * Subtract 1 from right.

![](2.png)

![](3.png)

![](4.png)

![](5.png)

![](6.png)

![](7.png)

![](8.png)

![](9.png)

![](10.png)

![](11.png)

![](12.png)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = left_max = right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(1)

[Prev](solution3.md)