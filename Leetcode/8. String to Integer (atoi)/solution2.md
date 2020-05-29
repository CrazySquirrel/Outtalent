# Direct approach

## Algorithm:

1. Create i pointer
2. Move i pointer until it reaches first non-space character or the end of the string
3. If i pointer reaches the end of the string or i character not in the set {'-','+','1','2','3','4','5','6','7','8','9','0'} then return 0
3. Set Is_negative flag to true if i character is minus
4. If i character in set {'-','+'} then move i pointer by 1
5. If i pointer reaches the end of the string or i character not in the set {'1','2','3','4','5','6','7','8','9','0'} then return 0
6. Create res variable and set it to 0, then start moving i pointer until it reaches the end of the string or first non-digit character and check:
    1. Get current digit 
    2. if res less than INT_MIN / 10 then return INT_MIN
    3. if res if equal to INT_MIN / 10 and digit greater than 8 then return INT_MIN
    4. if res greater than INT_MAX / 10 then return INT_MAX
    5. if res if equal to INT_MAX / 10 and digit greater than 7 then return INT_MAX
    7. Return + or - res based on Is_negative flag

```python
INT_MAX = 2147483647
INT_MIN = 2147483648  # without sign

NUM_SET = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
SIGN_SET = {'-', '+'}
NUM_START_SET = SIGN_SET | NUM_SET

ZERO = ord('0')


class Solution:
    def myAtoi(self, S: str) -> int:
        if not S: return 0

        i = 0

        while i < len(S) and S[i] == ' ': i += 1

        if i == len(S) or S[i] not in NUM_START_SET: return 0

        is_negative = S[i] == '-'

        if S[i] in SIGN_SET: i += 1

        if i == len(S) or S[i] not in NUM_SET: return 0

        res = 0

        while i < len(S) and S[i] in NUM_SET:
            digit = ord(S[i]) - ZERO

            if is_negative:
                if res > INT_MIN // 10 or (res == INT_MIN // 10 and digit > 8): return -INT_MIN
            else:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7): return INT_MAX

            res = res * 10 + digit

            i += 1

        return -res if is_negative else res
```

## Complexity Analysis

* Time Complexity: O(n)

Where n is the length of the string

* Space Complexity: O(1)

[Prev](solution1.md)