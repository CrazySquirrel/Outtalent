from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        result = -1
        for k, v in counter.items():
            if k == v: result = max(result, k)
        return result
