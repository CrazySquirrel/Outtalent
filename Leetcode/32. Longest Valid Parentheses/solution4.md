# Without extra space

## Algorithm

* Create left and right index and set them to 0
* Iterate i from 0 to length of s:
    * If s[i] = '(' then increment left otherwise increment right
    * If left equal to right set result to the max of result and 2 * right
    * If right grater than left set left and right to 0
* Set left and right to 0
* Iterate i from length of s to 0:
    * If s[i] = '(' then increment left otherwise increment right
    * If left equal to right set result to the max of result and 2 * left
    * If left grater than right set left and right to 0
* Return result

![](20.png)

![](21.png)

![](22.png)

![](23.png)

![](24.png)

![](25.png)

![](26.png)

![](27.png)

![](28.png)

![](29.png)

![](30.png)

![](31.png)

![](32.png)

![](33.png)

![](34.png)

![](35.png)

![](36.png)

![](37.png)

![](38.png)

![](39.png)

![](40.png)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0

        left = right = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                result = max(result, 2 * right)
            elif right >= left:
                left = right = 0

        left = right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                result = max(result, 2 * left)
            elif left >= right:
                left = right = 0

        return result
```

## Complexity Analysis

Time complexity: O(n)

Space complexity: O(1)

[Prev](solution3.md)