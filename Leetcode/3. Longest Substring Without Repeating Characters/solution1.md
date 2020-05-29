# Brute Force

## Intuition

Check all the substring one by one to see if it has no duplicate character.

## Algorithm

Suppose we have a function boolean allUnique(String substring) which will return true if the characters in the substring are all unique, otherwise false. We can iterate through all the possible substrings of the given string s and call the function allUnique. If it turns out to be true, then we update our answer of the maximum length of substring without duplicate characters.

Now let's fill the missing parts:

1. To enumerate all substrings of a given string, we enumerate the start and end indices of them. Suppose the start and end indices are i and j, respectively. Then we have 0≤i<j≤n (here end index j is exclusive by convention). Thus, using two nested loops with i from 0 to n−1 and j from i+1 to n, we can enumerate all the substrings of s.

2. To check if one string has duplicate characters, we can use a set. We iterate through all the characters in the string and put them into the set one by one. Before putting one character, we check if the set already contains it. If so, we return false. After the loop, we return true.

```python
class Solution:
    def allUnique(self, s: str, start: int, end: int) -> bool:
        h = set()

        for i in range(start, end):
            if s[i] in h: return False
            h.add(s[i])

        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.allUnique(s, i, j):
                    ans = max(ans, j - i)

        return ans
```

## Complexity Analysis

* Time complexity: O(n<sup>3</sup>).

To verify if characters within index range [i,j) are all unique, we need to scan all of them. Thus, it costs O(j−i) time.

For a given i, the sum of time costed by each j∈[i+1,n] is

![](1.png)

Thus, the sum of all the time consumption is:

![](2.png)

* Space complexity: O(min(n,m)).

We need O(k) space for checking a substring has no duplicate characters, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.

[Next](solution2.md)