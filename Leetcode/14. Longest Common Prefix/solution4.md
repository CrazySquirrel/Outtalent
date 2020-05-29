# Binary search

The idea is to apply binary search method to find the string with maximum value L, which is common prefix of all of the strings. 
The algorithm searches space is the interval (0…minLen), where minLen is minimum string length and the maximum possible common prefix. 
Each time search space is divided in two equal parts, one of them is discarded, because it is sure that it doesn't contain the solution. 
There are two possible cases:

* S[1...mid] is not a common string. This means that for each j > i S[1..j] is not a common string and we discard the 
second half of the search space.
* S[1...mid] is common string. This means that for for each i < j S[1..i] is a common string and we discard the first 
half of the search space, because we try to find longer common prefix

![](3.png)

```python
class Solution:
    def isCommonPrefix(self, strs: List[str], l: int) -> bool:
        prefix = strs[0][:l]
        for i in range(1, len(strs)):
            if strs[i].find(prefix) != 0:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        l, h = 1, min([len(s) for s in strs])
        while l <= h:
            m = l + (h - l) // 2
            if self.isCommonPrefix(strs, m):
                l = m + 1
            else:
                h = m - 1
        return strs[0][:l + (h - l) // 2]
```

## Complexity Analysis

In the worst case we have n equal strings with length m

* Time complexity: O(S⋅logm)

Where S is the sum of all characters in all strings.

The algorithm makes logm iterations, for each of them there are S=m⋅n comparisons, which gives in total O(S⋅logm) time complexity.

* Space complexity: O(1).

We only used constant extra space.

[Prev](solution3.md) [Next](solution5.md)