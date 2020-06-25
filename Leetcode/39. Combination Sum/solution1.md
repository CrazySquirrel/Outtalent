# DFS

## Algorithm

* Save length of candidates to l
* Create an empty result list
* DFS (target, index, path):
    * If target less then 0 return None
    * If target equal to 0 then append path to result
    * Iterate i from index to l:
        * If candidates[i] > target break iteration
        * Do dfs(target - candidates[i], i, path + candidates[i])
* Return result

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)

        def dfs(target: int, index: int, path: List[int]) -> None:
            if target < 0: return None
            if target == 0: return result.append(path)
            for i in range(index, l):
                if candidates[i] > target: break
                dfs(target - candidates[i], i, path + [candidates[i]])

        result = []
        candidates.sort()

        dfs(target, 0, [])

        return result
```

## Complexity Analysis

* Time complexity: O(k * n<sup>2</sup>)

* Space complexity: O(k * n)