# Min max compare

## Algorithm

1. Get min string s1 and max string s2 (according to lexicographical order)
2. Traverse i from 0 to min(s1,s2):
    1. If s1[i] != s2[i] then return s1[0..i]
3. If prefix of both strings is equal then return smallest string

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        w1, w2 = min(strs), max(strs)

        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]: return w1[:i]

        return w1 if len(w1) < len(w2) else w2
```

## Complexity Analysis

* Time complexity: O(N + S)

* Space complexity: O(S)

Where N is length of strings list and S is min(s1,s2)

[Prev](solution4.md) [Next](solution6.md)