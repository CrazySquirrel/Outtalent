# Approach 1

## Algorithm

* Create result = [1]
* Iterate from 0 to n - 1:
    * Set next = []
    * Iterate num in result:
        * If next is empty or last element in next not equal to num then add 1 and num to next else increment penultimate element in nums
    * Set result to next
* Return result

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        result = [1]
        for _ in range(n - 1):
            next = []
            for num in result:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
                result = next
        return "".join(map(str, result))
```

## Complexity Analysis

* Time complexity: O(m * n)

* Space complexity: O(n)

Where m is the string length.