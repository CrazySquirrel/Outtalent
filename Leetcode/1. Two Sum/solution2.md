# Two-pass Hash Table

To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

We reduce the look up time from O(n) to O(1) by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred, a look up could degenerate to O(n) time. But look up in hash table should be amortized O(1) time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement (target−nums[i]) exists in the table. Beware that the complement must not be nums[i] itself!

## Solutions:

* [Python](./solution2.py)
* [Java](./solution2.java)
* [C++](./solution2.cpp)

## Complexity Analysis:

* Time complexity: O(n).

We traverse the list containing n elements exactly twice. Since the hash table reduces the look up time to O(1), the time complexity is O(n).

* Space complexity: O(n).

The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.

[Prev](solution1.md) [Next](solution3.md)