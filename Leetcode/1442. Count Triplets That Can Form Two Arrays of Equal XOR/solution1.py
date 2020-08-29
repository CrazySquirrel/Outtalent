class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        @lru_cache(None)
        def getXor(l, h):
            result = arr[l]
            for i in range(l + 1, h + 1): result ^= arr[i]
            return result

        result = []

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if getXor(i, j - 1) == getXor(j, k):
                        result.append((i, j, k))

        return len(result)
