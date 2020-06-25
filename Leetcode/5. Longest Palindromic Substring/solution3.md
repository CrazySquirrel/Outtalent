# Manacher’s Algorithm

## Algorithm

* If string length less than 2 or string is a palindrome then just return string
* Initialize start as 0 and maxlen as 1 since smallest palindrome can contain only one symbol and start at position 1 
* Iterate through string:
    * Get odd start index as i - maxlen - 1
    * Get odd string as s[oddstart:i + 1]
    * If odd string is palindrome set start as odd start index and increase maxlen by 2
    
    * Get even start index as i - maxlen
    * Get even string as s[evenstart:i + 1]
    * If even string is palindrome set start as even start index and increase maxlen by 1
* Return s[start:start + maxlen]

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]: return s

        start, maxlen = 0, 1

        for i in range(len(s)):
            oddstart = i - maxlen - 1
            odd = s[oddstart:i + 1]

            if oddstart >= 0 and odd == odd[::-1]:
                start = oddstart
                maxlen += 2
                continue

            evenstart = i - maxlen
            even = s[evenstart:i + 1]

            if evenstart >= 0 and even == even[::-1]:
                start = evenstart
                maxlen += 1
                continue

        return s[start:start + maxlen]
```

## Complexity Analysis

* Time complexity: O(n). 

* Space complexity: O(1). 

[Prev](solution2.md)