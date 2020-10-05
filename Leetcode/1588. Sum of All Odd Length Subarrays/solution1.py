class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                result += sum(arr[j:j + i])
        return result
