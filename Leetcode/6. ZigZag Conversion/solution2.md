# Visit by Row

## Intuition

Visit the characters in the same order as reading the Zig-Zag pattern line by line.

## Algorithm

Visit all characters in row 0 first, then row 1, then row 2, and so on...

For all whole numbers k,

* Characters in row 0 are located at indexes k(2⋅numRows−2)
* Characters in row numRows−1 are located at indexes k(2⋅numRows−2)+numRows−1
* Characters in inner row i are located at indexes k(2⋅numRows−2)+i and (k+1)(2⋅numRows−2)−i.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        result = ''
        n = len(s)
        cycle_len = 2 * numRows - 2

        for i in range(numRows):
            for j in range(0, n - i, cycle_len):
                result += s[j + i]

                if i != 0 and i != numRows - 1 and j + cycle_len - i < n:
                    result += s[j + cycle_len - i]

        return result
```

## Complexity Analysis

* Time Complexity: O(n), where n==len(s). 

Each index is visited once.

* Space Complexity: O(n). 

For the cpp implementation, O(1) if return string is not considered extra space.

[Prev](solution1.md) [Next](solution3.md)