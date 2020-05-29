# Closure Number

## Algorithm

For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1. Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        result = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - c - 1):
                    result.append('({}){}'.format(left, right))
        return result
```

## Complexity Analysis

* Time Complexity: ![](3.png)

* Space Complexity: ![](3.png)

The analysis is similar to [Approach 2](solution2.md).

[Prev](solution2.md)