# Brute Force

The brute force approach is simple. Loop through each element x and find if there is another value that equals to target−x.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        raise ValueError('No two sum solution')
```

## Complexity Analysis

* Time complexity: O(n<sup>2</sup>). 

For each element, we try to find its complement by looping through the rest of array which takes O(n) time. Therefore, the time complexity is O(n<sup>2</sup>).

* Space complexity: O(1).

[Next](solution2.md)