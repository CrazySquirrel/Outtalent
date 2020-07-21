class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0

        for x in range(32)[::-1]:
            mask += 1 << x
            prefix = set([n & mask for n in nums])
            temp = ans | 1 << x

            for p in prefix:
                if temp ^ p in prefix:
                    ans = temp
                    break

        return ans
