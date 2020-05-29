# Horizontal scanning

## Algorithm

To employ this idea, the algorithm iterates through the strings [S<sub>1</sub>...S<sub>n</sub>], finding at each iteration 
i the longest common prefix of strings LCP(S<sub>1</sub>...S<sub>i</sub>). When LCP(S<sub>1</sub>...S<sub>i</sub>) is 
an empty string, the algorithm ends. Otherwise after n iterations, the algorithm returns LCP(S<sub>1</sub>...S<sub>n</sub>).

![](1.png)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix: return ''
        return prefix
```

## Complexity Analysis

* Time complexity: O(S), where S is the sum of all characters in all strings.

In the worst case all n strings are the same. The algorithm compares the string S1 with the other strings [S<sub>1</sub>...S<sub>i</sub>] 
There are S character comparisons, where S is the sum of all characters in the input array.

* Space complexity: O(1).

We only used constant extra space.

[Next](solution2.md)