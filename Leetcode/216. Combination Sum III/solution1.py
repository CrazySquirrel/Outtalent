class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l, h = 1, 9

        def helper(l: int, k: int, n: int) -> List[List[int]]:
            if k == 1: return [[n]] if l <= n <= h else []

            result = []

            for i in range(l, h):
                for sub_result in helper(max(i, l) + 1, k - 1, n - i):
                    result.append([i] + sub_result)

            return result

        return helper(l, k, n)
