# Iterative approach

## Algorithm

1. Create to lists for roman and arabic number
> ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
>
> [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
2. Iterate through both of lists and check:
    1. Get quotient of the division remaining number by current arabic number
    2. Reduce remainder by multiplication of current arabic number and quotient
    3. Add to result quotient of current roman number

```python
ROMAN = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
INTEGERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        for i, r in zip(INTEGERS, ROMAN):
            count = num // i
            num -= i * count
            result += r * count
        return result
```

## Complexity Analysis

* Time complexity: O(1)<sup>*</sup>. 

* Space complexity: O(1)<sup>*</sup>.

<sup>*</sup> - We need time and space to create lists of arabic and roman numbers and iterate over them, but it'll always be constant

[Next](solution2.md)