# Approach 1

## Algorithm

* Create 9 sets for rows, 9 for cols and 9 for squares
* Fill rows, cols and squares sets with numbers that missed in each row, col and square
* Got to dfs with board, rows, cols and squares

### DFS:

* Iterate i from 0 to 9:
    * Iterate j from 0 to 9:
        * If board[i][j] is not '.' skip
        * Get k as i / 3 * 3 + j / 3
        * Get choices as intersection of rows[i] & cols[j] & squares[k]
        * If there is no choices return false
        * Iterate c in choices:
            * Set board[i][j] to c
            * Remove c from rows[i], cols[j] and squares[k]
            if dfs(board, rows, cols, squares) then return true
            * Add c to rows[i], cols[j] and squares[k]
            * Set board[i][j] to '.'
        * Return false
* Return true

```python
class Solution:
    def dfs(self, board, rows, cols, grid):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': continue
                k = i // 3 * 3 + j // 3
                choices = rows[i] & cols[j] & grid[k]
                if not choices: return False
                for c in choices:
                    board[i][j] = c
                    rows[i].remove(c)
                    cols[j].remove(c)
                    grid[k].remove(c)
                    if self.dfs(board, rows, cols, grid): return True
                    rows[i].add(c)
                    cols[j].add(c)
                    grid[k].add(c)
                    board[i][j] = '.'
                return False
        return True

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        full = set(map(str, range(1, 10)))
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[i // 3 * 3 + j // 3].add(board[i][j])

        rows = [full - row for row in rows]
        cols = [full - col for col in cols]
        grid = [full - cell for cell in grid]

        self.dfs(board, rows, cols, grid)
```

## Complexity Analysis

* Time complexity: O(9<sup>n<sup>2</sup></sup>)

* Space complexity: O(n)

[Next](solution2.md)