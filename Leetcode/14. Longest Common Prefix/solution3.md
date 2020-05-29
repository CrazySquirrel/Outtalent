# Divide and conquer

## Algorithm

To apply the observation above, we use divide and conquer technique, where we split the LCP(S<sub>i</sub>...S<sub>j</sub>) 
problem into two subproblems LCP(S<sub>i</sub>...S<sub>mid</sub>) and LCP(S<sub>mid+1</sub>...S<sub>j</sub>), where mid is  
(i+j)/2. We use their solutions lcpLeft and lcpRight to construct the solution of the main problem LCP(S<sub>i</sub>...S<sub>j</sub>).
To accomplish this we compare one by one the characters of lcpLeft and lcpRight till there is no character match.
The found common prefix of lcpLeft and lcpRight is the solution of the LCP(S<sub>i</sub>...S<sub>j</sub>).

![](2.png)

```python
class Solution:
    def commonPrefix(self, left: str, right: str) -> str:
        m = min(len(left), len(right))
        for i in range(m):
            if left[i] != right[i]:
                return left[:i]
        return left[:m]

    def helper(self, strs: List[str], l: int, r: int) -> str:
        if l == r: return strs[l]
        m = l + (r - l) // 2
        lcp_left = self.helper(strs, l, m)
        lcp_right = self.helper(strs, m + 1, r)
        return self.commonPrefix(lcp_left, lcp_right)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        return self.helper(strs, 0, len(strs) - 1)
```

## Complexity Analysis

In the worst case we have n equal strings with length m

* Time complexity: O(S)

Where S is the number of all characters in the array, S=m⋅n Time complexity is 2⋅T(n/2)+O(m). 
Therefore time complexity is O(S). In the best case this algorithm performs O(minLen⋅n) comparisons, where minLen is 
the shortest string of the array

* Space complexity : O(m⋅logn)

There is a memory overhead since we store recursive calls in the execution stack. 
There are logn recursive calls, each store need m space to store the result, so space complexity is O(m⋅logn)

[Prev](solution2.md) [Next](solution4.md)