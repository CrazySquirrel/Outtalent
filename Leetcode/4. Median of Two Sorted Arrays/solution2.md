# Two pointer binary search

## Algorithm

* Get lengths m and n of arrays a and b
* If array a is bigger then b then switch m and n and a and b so second array always will be bigger
* Create two indexes l = 0 and r = n (length of the smallest array)
* Iterate while l less or equal to r:
    * Get indexes i as l + (r - l) / 2 and index j as (n + m + 1) / 2 - i
    * If i < n and j > 0 and b[j - 1] > a[i] then l = i + 1
    * If i > 0 and j < m and b[j] < a[i - 1] then r = i - 1
    * Else:
        * if i = 0 then median = b[j - 1]
        * if j == 0 then median = a[i - 1]
        * else median = max of a[i - 1] and b[j - 1]
        
        * If length of two arrays is odd then return median
        * if i = n then return (median + b[j]) / 2
        * if j == m then return (median + a[i]) / 2
        * Otherwise return (median + min(a[i], b[j])) / 2

```python
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n, m = len(a), len(b)
        if n > m: a, b, m, n = b, a, n, m
        l, r = 0, n
        if n == 0: raise ValueError
        while l <= r:
            i = l + (r - l) // 2
            j = (n + m + 1) // 2 - i
            if i < n and j > 0 and b[j - 1] > a[i]:
                l = i + 1
            elif i > 0 and j < m and b[j] < a[i - 1]:
                r = i - 1
            else:
                if i == 0:
                    median = b[j - 1]
                elif j == 0:
                    median = a[i - 1]
                else:
                    median = max(a[i - 1], b[j - 1])
                break
        if (n + m) % 2 == 1: return median
        if i == n: return (median + b[j]) / 2
        if j == m: return (median + a[i]) / 2
        return (median + min(a[i], b[j])) / 2
```

## Complexity Analysis

* Time complexity: O(log(min(m,n))). 

* Space complexity: O(1).

[Prev](solution1.md) [Next](solution3.md)