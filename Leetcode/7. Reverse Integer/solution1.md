# Pop and Push Digits & Check before Overflow

## Intuition

We can build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow.

## Algorithm

Reversing an integer can be done similarly to reversing a string.

We want to repeatedly "pop" the last digit off of x and "push" it to the back of the rev. In the end, rev will be the reverse of the x.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.

```
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```

However, this approach is dangerous, because the statement temp=rev⋅10+pop can cause overflow.

Luckily, it is easy to check beforehand whether or this statement would cause an overflow.

To explain, lets assume that rev is positive.

1. If temp=rev⋅10+pop causes overflow, then it must be that rev ≥ INTMAX/10
2. If rev > INTMAX/10, then temp=rev⋅10+pop is guaranteed to overflow.
3. If rev == INTMAX/10, then temp=rev⋅10+pop will overflow if and only if pop>7

Similar logic can be applied when rev is negative.

```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = 2147483648  # without sign

        s = -1 if x < 0 else 1

        x = abs(x)
        rev = 0

        while x:
            pop = x % 10
            x //= 10

            if s == 1:
                if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7): return 0
            else:
                if rev > INT_MIN // 10 or (rev == INT_MIN // 10 and pop > 8): return 0

            rev = rev * 10 + pop

        return rev * s
```

## Complexity Analysis

* Time Complexity: O(log(x)). 

There are roughly log<sub>10</sub>(x) digits in x.

* Space Complexity: O(1).

[Next](solution2.md)