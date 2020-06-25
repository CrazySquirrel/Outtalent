# Boyer–Moore

## Algorithm

* Get alphabet from haystack
* Find the last appearance of each character in needle
* Save length of needle to n and length of haystack to m
* Set i = n - 1 and j = n - 1
* Iterate while i < m:
    * If haystack[i] == needle[j]:
        * if j = 0 then return i else decrement i and j
    * else:
        * set l = last[haystack[i]]
        * set i = i + n - min(j, 1 + l)
        * set j = n - 1
* Return -1

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1

        alphabet = set(haystack)

        last = {letter: needle.rfind(letter) for letter in alphabet}

        n = len(needle)
        m = len(haystack)

        i = n - 1
        j = n - 1

        while i < m:
            if haystack[i] == needle[j]:
                if j == 0:
                    return i
                else:
                    i -= 1
                    j -= 1
            else:
                l = last[haystack[i]]
                i = i + n - min(j, 1 + l)
                j = n - 1

        return -1
```

## Complexity Analysis:

* Time complexity: O(n * m) -> O(m/n)

* Space Complexity: O(m)

[Prev](solution4.md)