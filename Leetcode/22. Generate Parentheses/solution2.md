# Backtracking

## Algorithm

Instead of adding '(' or ')' every time as in [Approach 1](solution1.md), let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                result.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return result
```

## Complexity Analysis

Our complexity analysis rests on understanding how many elements there are in ```generateParenthesis(n)```. 
This analysis is outside the scope of this article, but it turns out this is the n-th Catalan number ![](1.png),
which is bounded asymptotically by ![](2.png)

* Time Complexity: ![](3.png)

Each valid sequence has at most n steps during the backtracking procedure.

* Space Complexity: ![](3.png)

As described above, and using O(n) space to store the sequence.

[Prev](solution1.md) [Next](solution3.md)