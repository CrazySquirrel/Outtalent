class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result, n = 0, len(arr)
        for i in range(n - 1):
            accumulator = arr[i]
            for k in range(i + 1, n):
                accumulator ^= arr[k]
                if accumulator == 0: result += k - i
        return result
