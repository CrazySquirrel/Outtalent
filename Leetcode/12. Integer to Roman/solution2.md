# Mathematical approach

## Algorithm

1. Create 4 lists V1-V4:

> ["", "M", "MM", "MMM"]
>
> ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
>
> ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
>
> ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
>
2. Do some math:
    1. Thousands will be equal ```V1[num // 1000]```
    2. Hundreds will be equal ```V2[(num % 1000) // 100]```
    3. Tens will be equal ```V3[(num % 100) // 10]```
    4. Units will be equal ```V4[num % 10]```

```python
V1 = ["", "M", "MM", "MMM"]
V2 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
V3 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
V4 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


class Solution:
    def intToRoman(self, num: int) -> str:
        return V1[num // 1000] + V2[(num % 1000) // 100] + V3[(num % 100) // 10] + V4[num % 10];
```

## Complexity Analysis

* Time complexity: O(1)<sup>*</sup>. 

* Space complexity: O(1)<sup>*</sup>.

<sup>*</sup> - We need time and space to create V1-V4 lists, but it'll always be constant

[Prev](solution1.md)
