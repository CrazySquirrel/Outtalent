# Vertical scanning

## Algorithm

Imagine a very short string is at the end of the array. The above approach will still do S comparisons. 
One way to optimize this case is to do vertical scanning. We compare characters from top to bottom on the same column 
(same character index of the strings) before moving on to the next column.

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
```

## Complexity Analysis

* Time complexity: O(S), 

where S is the sum of all characters in all strings. 
In the worst case there will be n equal strings with length m and the algorithm performs S=m⋅n character comparisons. 
Even though the worst case is still the same as [Approach 1](solution1.md), in the best case there are at most n⋅minLen comparisons 
where minLen is the length of the shortest string in the array.

* Space complexity: O(1). 

We only used constant extra space.

[Prev](solution1.md) [Next](solution3.md)