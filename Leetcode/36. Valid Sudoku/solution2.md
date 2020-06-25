# Approach 2

* Create 9 sets for rows, 9 for cols and 9 for squares
* Iterate i from 0 to 9:
    * Iterate j from 0 to 9:
        * If board[i][j] = '.' skip
        * Get square index as i / 3 * 3 + j / 3
        * If board[i][j] in row[i], col[j] or grid[ind] then return false
        * Add board[i][j] to row[i], col[j] and grid[ind]
* Return true

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                e = board[i][j]

                if e == '.': continue

                ind = i // 3 * 3 + j // 3

                if e in (row[i] | col[j] | grid[ind]): return False

                row[i].add(e)
                col[j].add(e)
                grid[ind].add(e)

        return True
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(n)

[Prev](solution1.md)