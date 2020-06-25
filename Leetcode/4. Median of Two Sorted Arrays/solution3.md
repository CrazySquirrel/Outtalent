# K-th method

## Algorithm

* If length of two arrays is odd then return k-th element (where k is in the middle) 
* If length of two arrays is even then return (k + k<sub>-1</sub>)/2 (where k is in the middle and k<sub>-1</sub> element less than k)

* To find k element:
    * Create ai = 0, al = length of a, bi = 0, bl = length of b, k = (length of a + length of b)/2
    * Iterate:
        * if al - ai < 0 then return B[k + bi]
        * if bl - bi < 0 then return A[k + ai]
        * if k < 1 then return min of A[k + ai] and B[k + bi]
        
        * Get indexes am and bm as (ai + al) / 2 and (bi + bl) / 2
        * Get av and bv as A[am] and B[bm]
        
        * if (am - ai) + (bm - bi) < k:
            * if av > bv then:
                * k = k - (bm - bi) - 1 and bi = bm + 1
            * else:
                * k = k - (am - ai) - 1 and ai = am + 1
        * else:
            * if av > bv then:
                * al = am - 1 
            * else:
                * bl = bm - 1
            

```python
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        lens = len(A) + len(B)

        def kth(ai: int, al: int, bi: int, bl: int, k: int):
            while True:
                if al - ai < 0: return B[k + bi]
                if bl - bi < 0: return A[k + ai]
                if k < 1: return min(A[k + ai], B[k + bi])
                am, bm = (ai + al) // 2, (bi + bl) // 2
                av, bv = A[am], B[bm]
                if (am - ai) + (bm - bi) < k:
                    if av > bv:
                        k = k - (bm - bi) - 1
                        bi = bm + 1
                    else:
                        k = k - (am - ai) - 1
                        ai = am + 1
                else:
                    if av > bv:
                        al = am - 1
                    else:
                        bl = bm - 1

        if lens % 2 == 1:
            return kth(0, len(A) - 1, 0, len(B) - 1, lens // 2)
        else:
            return (kth(0, len(A) - 1, 0, len(B) - 1, lens // 2) + kth(0, len(A) - 1, 0, len(B) - 1, lens // 2 - 1)) / 2
```

## Complexity Analysis

* Time complexity: O(log(min(m,n))). 

* Space complexity: O(1).

[Prev](solution2.md)