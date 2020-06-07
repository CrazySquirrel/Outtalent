class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        nums = [int("".join(row), base=2) for row in matrix]

        result = 0

        for i in range(len(nums)):
            cur = -1

            for j in range(i, len(nums)):
                cur &= nums[j]

                if cur == 0: break

                count = 0
                tmp = cur

                while tmp:
                    count += 1
                    tmp &= tmp >> 1

                result = max(result, count * (j - i + 1))

        return result
