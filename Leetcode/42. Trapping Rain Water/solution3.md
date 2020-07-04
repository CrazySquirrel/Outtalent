# Using stacks

## Algorithm

* Use stack to store the indices of the bars.
* Iterate the array:
    * While stack is not empty and height[current]>height[st.top()]
        * It means that the stack element can be popped. Pop the top element as top.
        * Find the distance between the current element and the element at top of stack, which is to be filled. distance=current−st.top()−1
        * Find the bounded height bounded_height=min(height[current],height[st.top()])−height[top]
        * Add resulting trapped water to answer ans+=distance×bounded_height
    * Push current index to top of the stack
    * Move current to the next position

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        s = []

        result = 0

        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                top = s.pop()
                if not s: break
                distance = i - s[-1] - 1
                bounded_height = min(height[i], height[s[-1]]) - height[top]
                result += distance * bounded_height
            s.append(i)

        return result
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(n)

[Prev](solution2.md) [Next](solution4.md)