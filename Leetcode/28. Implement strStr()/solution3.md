# Rolling Hash

## Algorithm

* Create hash function of string S:
    * Set l to length of S
    * Sum all expressions from 0 to length of S:
        * Where expression is ((ASCII code of character S[i]) * base1<sup>l - 1 - i</sup>)
        
* Create rolling hash function of old_hash, old_value and new_value:
    * Return (old_hash - (ASCII code of old_value) * base2) * base1 + (ASCII code of new_value)

* Set m to length of haystack and n to length of needle
* Set base1 to sum big prime number (for example 401)
* Set base2 to base1<sup>n - 1</sup>
* Get n_hash of needle and m_hash of haystack from 0 to n
* Iterate from 1 to m - n + 1:
    * Get m_hash = rolling_hashing(m_hash, haystack[i - 1], haystack[i + n - 1])
    * If m_hash = n_hash then return i
* Return -1

```python
class Solution:
    def hashing(self, S: str) -> int:
        l = len(S)
        return sum([ord(S[i]) * (self.base1 ** (l - 1 - i)) for i in range(l)])

    def rolling_hashing(self, old_hash: int, old_value: str, new_value: str) -> int:
        return (old_hash - ord(old_value) * self.base2) * self.base1 + ord(new_value)

    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        self.base1 = 401
        self.base2 = self.base1 ** (n - 1)

        n_hash = self.hashing(needle)
        m_hash = self.hashing(haystack[0:n])

        if m_hash == n_hash: return 0

        for i in range(1, m - n + 1):
            m_hash = self.rolling_hashing(m_hash, haystack[i - 1], haystack[i + n - 1])
            if m_hash == n_hash: return i

        return -1
```

## Complexity Analysis:

* Time complexity: O(m + n)

* Space Complexity: O(1)

[Prev](solution2.md) [Next](solution4.md)