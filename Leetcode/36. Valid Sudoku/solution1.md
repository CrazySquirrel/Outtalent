# Approach 1

## Algorithm

* Go through rows and check if each row contain only unique numbers with set
* Go through cols and check if each col contain only unique numbers with set
* Go through squares and check if each col contain only unique numbers with set

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for cell in row:
                if cell == '.': continue
                if cell in s: return False
                s.add(cell)

        for col in zip(*board):
            s = set()
            for cell in col:
                if cell == '.': continue
                if cell in s: return False
                s.add(cell)

        for i in range(0, 10, 3):
            for j in range(0, 10, 3):
                s = set()
                for row in board[i:i + 3]:
                    for cell in row[j:j + 3]:
                        if cell == '.': continue
                        if cell in s: return False
                        s.add(cell)

        return True
```

## Complexity Analysis

* Time complexity: O(n)

* Space complexity: O(n)

[Next](solution2.md)