# Simple Recursion

## Algorithm

* Check if string is a palindrome. If so then just return string
* If string is not a palindrome then try recursively s[1:] and s[:-1] and return longest result

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        return max(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]), key=lambda x: len(x))
```

The problem with this solution is that we going to check some string multiple times:

```
abcde -> bcde -> cde
              -> bcd *
      -> abcd -> bcd *
              -> abc
```

## Complexity Analysis

* Time complexity: O(2<sup>n</sup>).
* Space complexity: O(n).

[Next](solution2.md)