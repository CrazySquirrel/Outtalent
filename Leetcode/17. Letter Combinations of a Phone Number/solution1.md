# Backtracking

[Backtracking](https://en.wikipedia.org/wiki/Backtracking) is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function backtrack(combination, next_digits) which takes as arguments an ongoing letter combination and the next digits to check.

* If there is no more digits to check that means that the current combination is done.
* If there are still digits to check :
    * Iterate over the letters mapping the next available digit.
        * Append the current letter to the current combination combination = combination + letter.
        * Proceed to check next digits : backtrack(combination + letter, next_digits[1:]).

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def backtrack(combination, next_digits):
            if not next_digits:
                output.append(combination)
            else:
                for letter in phone[int(next_digits[0])]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output
```

## Complexity Analysis

* Time complexity : O(3<sup>N</sup> * 4<sup>M</sup>) 

Where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.

* Space complexity : O(3<sup>N</sup> * 4<sup>M</sup>) 
 
Since one has to keep 3<sup>N</sup> * 4<sup>M</sup> solutions.

[Next](solution2.md)