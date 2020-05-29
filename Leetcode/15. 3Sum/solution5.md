# Split negative and positive

## Algorithm

1. Count each numbers in nums list
2. If there are more than three 0 in nums then add [0,0,0] to the results
3. Create two lists for positive and negative numbers from nums
4. Iterate through unique numbers from nums and add them to negative or positive list respectively
5. Iterate through negative numbers:
    1. Iterate through positive numbers:
        1. Get x as - negative number - positive number
        2. If x exist in nums and x not the same as negative number or positive number then add negative, x and positive number to the results
6. Return results

```python
class Solution:
    def threeSum(self, nums):
        counter = {}
        negative, positive = set(), set()

        for x in nums:
            if x not in counter:
                counter[x] = 0

            counter[x] += 1

            if x <= 0:
                negative.add(x)
            else:
                positive.add(x)

        result = set() if counter.get(0, 0) < 3 else {(0, 0, 0)}

        for n in negative:
            for p in positive:
                x = -n - p
                if x in counter and (x in {n, p} and counter[x] > 1 or n < x < p):
                    result.add((n, x, p))

        return result
```

## Complexity Analysis

* Time complexity: O(n + m<sup>2</sup>)

* Space complexity: O(n + r)

Where: 
 * n is the length on nums list
 * m is the max length positive and negative numbers list
 * r is the length or result list

[Prev](solution4.md) [Next](solution6.md)