# Simulation

## Algorithm

The key to solve this problem is multiplying each digit of the numbers at the corresponding positions and get the sum values at each position. That is how we do multiplication manually.

![](1.jpg)

![](2.jpg)

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = ord('0')
        m, n = len(num1), len(num2)
        vals = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - zero) * (ord(num2[j]) - zero)
                p1, p2 = i + j, i + j + 1
                s = mul + vals[p2]
                vals[p1] += s // 10
                vals[p2] = s % 10

        res = ''

        for val in vals:
            if res or val != 0:
                res += chr(val + zero)

        return res if res else '0'
```

## Complexity Analysis

* Time complexity: O(n * m)

* Space complexity: O(n + m)