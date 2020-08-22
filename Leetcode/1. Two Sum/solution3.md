# One-pass Hash Table

It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

## Solutions:

* [Python](./solution3.py)
* [Java](./solution3.java)
* [C++](./solution3.cpp)

## Complexity Analysis:

* Time complexity: O(n). 

We traverse the list containing n elements only once. Each look up in the table costs only O(1) time.

* Space complexity: O(n).

The extra space required depends on the number of items stored in the hash table, which stores at most n elements.

[Prev](solution2.md) [Next](solution4.md)