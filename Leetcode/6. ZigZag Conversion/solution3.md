# Sort by Row (Optimized)

We going to use the same solution as for [Sort by Row](solution1.md) by with some coding optimizations.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s

        rows = [''] * numRows
        row_idx = 0
        direction = -1
        numRows -= 1

        for i, c in enumerate(s):
            rows[row_idx] += c
            if i % numRows == 0: direction *= -1
            row_idx += direction

        return ''.join(rows)
```

[Prev](solution2.md)