# Set and sort

## Algorithm

1. Turn nums to the set
2. Turn set back to list
3. Sort new list

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)
```

## Complexity analysis

* Time complextiy: O(n log n).

We need to traverse through the list at turn it to the set.
We need another n to traverse through the set.
And we need n log n to sort new list.

* Space complexity: O(n).

We need up to n for temporary set and list

[Next](solution2.md)