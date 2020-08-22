class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr: return k
        if k < arr[0]: return k
        k -= arr[0] - 1
        for i in range(1, len(arr)):
            m = arr[i] - arr[i - 1] - 1
            if k <= m: return arr[i - 1] + k
            k -= m
        return arr[-1] + k
