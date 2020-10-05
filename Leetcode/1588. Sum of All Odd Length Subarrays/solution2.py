class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums = arr[:]
        for i in range(1, len(arr)): sums[i] += sums[i - 1]

        def rangesum(i: int, j: int):
            return sums[j] - sums[i - 1] if i else sums[j]

        result = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                result += rangesum(j, j + i - 1)
        return result
