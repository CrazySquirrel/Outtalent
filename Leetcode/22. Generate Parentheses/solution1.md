# Brute Force

## Algorithm

To generate all sequences, we use a recursion. All sequences of length n is just '(' plus all sequences of length n-1, and then ')' plus all sequences of length n-1.

To check whether a sequence is valid, we keep track of balance, the net number of opening brackets minus closing brackets. If it falls below zero at any time, or doesn't end in zero, the sequence is invalid - otherwise it is valid.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A=[]):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
```

## Complexity Analysis

* Time Complexity: O(2<sup>2n</sup>n). 
 
For each of 2<sup>2n</sup> sequences, we need to create and validate the sequence, which takes O(n) work.

* Space Complexity: O(2<sup>2n</sup>n).

Naively, every sequence could be valid. See Approach 3 for development of a tighter asymptotic bound.

[Next](solution2.md)