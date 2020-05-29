# Sort by Row

## Intuition

By iterating through the string from left to right, we can easily determine which row in the Zig-Zag pattern that a character belongs to.

## Algorithm

We can use min(numRows,len(s)) lists to represent the non-empty rows of the Zig-Zag Pattern.

Iterate through s from left to right, appending each character to the appropriate row. The appropriate row can be tracked using two variables: the current row and the current direction.

The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        rows = [''] * min(numRows, len(s))
        cur_row = 0
        goind_down = False

        for c in s:
            rows[cur_row] += c

            if cur_row == 0 or cur_row == numRows - 1:
                goind_down = not goind_down

            cur_row += 1 if goind_down else -1

        result = ''

        for row in rows:
            result += row

        return result
```

## Complexity Analysis

* Time Complexity: O(n), where n==len(s)

* Space Complexity: O(n)

[Next](solution2.md)