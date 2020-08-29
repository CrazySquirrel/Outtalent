class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr = [0] + arr
        for i in range(len(arr) - 1): arr[i + 1] ^= arr[i]
        result = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]: result += j - i - 1
        return result
