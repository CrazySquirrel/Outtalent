class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = [[]]
        for n in nums:
            tmp = []
            for l in res:
                for i in range(len(l) + 1):
                    tmp.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break
            res = tmp
        return res
