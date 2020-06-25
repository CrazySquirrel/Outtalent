# Brute force

## Algorithm

* Iterate through all permutations of words:
    * Set start to 0
    * Iterate while permutation string in s:
        * Set start to position of permutation string in s starting from prev start position
        * If new start exist add it to the result
        * Increment start index
* Return result

```python
from itertools import permutations


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        if not all([word in s for word in words]): return []
        result = set()
        for substring in permutations(words):
            substring = ''.join(substring)
            start = 0
            while True:
                try:
                    start = s.index(substring, start)
                    result.add(start)
                    start += 1
                except ValueError as e:
                    break
        return result
```

## Complexity Analysis:

* Time complexity: O(N! * (M + S<sup>2</sup> * M))

- Where N! is for iterate through all permutations of words.
- Where M is the sum length of all words

- We need M to concat all words to substring
- We need S * M in a worst case to find substring in S
- Plus we need to find all words substrings in S

* Space Complexity: O(S + M)

Where S is length of string s. We need additional space for result 

[Next](solution2.md)