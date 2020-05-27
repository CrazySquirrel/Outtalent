class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * n
        for i in range(1, n): factorial[i] = i * factorial[i - 1]
        nums = list(map(str, range(1, n + 1)))
        result = []
        k -= 1
        for i in range(n, 0, -1):
            idx = k // factorial[i - 1]
            k %= factorial[i - 1]
            result.append(nums[idx])
            nums.pop(idx)
        return ''.join(result)
