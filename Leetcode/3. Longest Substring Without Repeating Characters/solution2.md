# Sliding Window

## Algorithm

The naive approach is very straightforward. But it is too slow. So how can we optimize it?

In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. If a substring s<sub>ij</sub>
from index i to j−1 is already checked to have no duplicate characters. We only need to check if s[j] is already in the substring s<sub>ij</sub>.

To check if a character is already in the substring, we can scan the substring, which leads to an O(n<sup>2</sup>) algorithm. But we can do better.

By using HashSet as a sliding window, checking if a character in the current can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i,j) to the right by 1 element, then it becomes [i+1,j+1) (left-closed, right-open).

Back to our problem. We use HashSet to store the characters in current window [i,j) (j=i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = set()
        ans = i = j = 0
        while i < n and j < n:
            if s[j] in h:
                h.remove(s[i])
                i += 1
            else:
                h.add(s[j])
                j += 1
                ans = max(ans, j - i)
        return ans
```

## Complexity Analysis

* Time complexity: O(2n)=O(n).

In the worst case each character will be visited twice by i and j.

* Space complexity: O(min(m,n)).

Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.

[Prev](solution1.md) [Next](solution3.md)