# Dynamic programming

To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

We define P(i,j) as following:

![](1.png)

Therefore,

![](2.png)

The base cases are:

![](3.png)

This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        l = r = 0
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and (j - i + 1) > (r - l + 1):
                    l, r = i, j
        return s[l:r + 1]
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>). 

This gives us a runtime complexity of O(n<sup>2</sup>).

* Space complexity: O(n<sup>2</sup>). 

It uses O(n<sup>2</sup>) space to store the table.

[Prev](solution1.md) [Next](solution3.md)