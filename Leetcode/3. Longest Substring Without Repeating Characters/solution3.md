# Sliding Window Optimized (HashMap)

The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.

The reason is that if s[j] have a duplicate in the range [i,j) with index j<sup>′</sup>, we don't need to increase i little by little. We can skip all the elements in the range [i,j<sup>′</sup>] and let i to be j<sup>′</sup> +1 directly.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = {}
        ans = i = 0
        for j in range(n):
            if s[j] in h:
                i = max(i, h[s[j]])
            ans = max(ans, j - i + 1)
            h[s[j]] = j + 1
        return ans
```

## Complexity Analysis

* Time complexity: O(n). 

Index j will iterate n times.

* Space complexity: O(min(m,n)). 

Same as the previous approach.

[Prev](solution2.md) [Next](solution4.md)