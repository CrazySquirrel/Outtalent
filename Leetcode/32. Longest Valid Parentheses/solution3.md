# Using Stack

## Algorithm

* Create stack with -1
* Iterate i from 0 to length of s:
    * If s[i] = '(' then append i to the stack
    * else:
        * Pop last element from stack
        * If there is no stack then append i to stack
        * Else set result to the max of result and i - last element in stack
* Return result

![](9.png)

![](10.png)

![](11.png)

![](12.png)

![](13.png)

![](14.png)

![](15.png)

![](16.png)

![](17.png)

![](18.png)

![](19.png)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        result = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result
```

## Complexity Analysis

Time complexity: O(n)

Space complexity: O(n)

[Prev](solution2.md) [Next](solution4.md)