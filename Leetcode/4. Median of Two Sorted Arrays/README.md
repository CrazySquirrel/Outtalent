# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

## Example 1:

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

## Example 2:

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Naive approach](solution1.md) | O(n+m+(n*m)log(n*m)) | v |
| [Two pointer binary search](solution2.md) | O(log(min(m,n))) | O(1) |
| [K-th method](solution3.md) | O(log(min(m,n))) | O(1) |

## Video

[![4. Median of Two Sorted Arrays](http://img.youtube.com/vi/XpcApNjZ1hE/0.jpg)](http://www.youtube.com/watch?v=XpcApNjZ1hE&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "4. Median of Two Sorted Arrays")
