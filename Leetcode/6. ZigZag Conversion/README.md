# [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

## Example 1:

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

## Example 2:

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Sort by Row](solution1.md) | O(n) | O(n) |
| [Visit by Row](solution2.md) | O(n) | O(n) |
| [Sort by Row (Optimized)](solution3.md) | O(n) | O(n) |

## Video

[![6. ZigZag Conversion](http://img.youtube.com/vi/7YjQx0ooKZI/0.jpg)](http://www.youtube.com/watch?v=7YjQx0ooKZI&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "6. ZigZag Conversion")