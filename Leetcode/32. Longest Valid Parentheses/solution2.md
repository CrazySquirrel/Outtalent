# Dynamic Programming

## Algorithm

* Create dp of zeros
* Iterate i from 1 to length of s:
    * If s[i] not equal to ')' just continue new iteration
    * If s[i-1] equal to '(':
        * If i >= 2 then dp[i] = dp[i - 2] + 2 else dp[i] = 2
    * If i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
        * If (i - dp[i - 1]) >= 2 then dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 else dp[i] = dp[i - 1] + + 2
    * Set result to max of result and dp[i]
* Return result

![](1.png)

![](2.png)

![](3.png)

![](4.png)

![](5.png)

![](6.png)

![](7.png)

![](8.png)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        result = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] != ')': continue

            if s[i - 1] == '(':
                if i >= 2:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                if (i - dp[i - 1]) >= 2:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2

            result = max(result, dp[i])

        return result
```

## Complexity Analysis

Time complexity: O(n)

Space complexity: O(n)

[Prev](solution1.md) [Next](solution3.md)