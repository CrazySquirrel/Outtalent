class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        X = reduce(lambda x, y: x ^ y, nums)
        mask = X & -X
        a = b = 0
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n
        return [a, b]
