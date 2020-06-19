class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(l: int, k: int, n: int) -> List[List[int]]:
            if k == 1: return [[n]] if l <= n <= 9 else []

            result = []

            for i in range(l, min(n, 9)):
                for sub_result in helper(max(i, l) + 1, k - 1, n - i):
                    result.append([i] + sub_result)

            return result

        return helper(1, k, n)
