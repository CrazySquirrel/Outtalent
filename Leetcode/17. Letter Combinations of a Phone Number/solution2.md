# Recursion

## Algorithm

* If there is no digits then return an empty array
* If there if only one digit then we can return only letters for this digit
* Otherwise:
    * Get result for all digits except last
    * Get letters for first digits
    * Combine two lists and return the result

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if len(digits) == 0: return []
        if len(digits) == 1: return list(phone[int(digits[0])])

        prev = self.letterCombinations(digits[:-1])
        suffix = list(phone[int(digits[-1])])

        return [j + i for j in prev for i in suffix]
```

## Complexity Analysis

* Time complexity : O(3<sup>N</sup> * m<sup>N</sup>) 

* Space complexity : O(3<sup>N</sup> * m<sup>N</sup>) 

[Prev](solution1.md)