class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(1, len(arr)):
            if arr[i - 1] - arr[i] != diff: return False
        return True
