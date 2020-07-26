class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp = set()
        for n in nums:
            for y in list(dp):
                if n >= y[-1]: dp.add(y + (n,))
            dp.add((n,))
        return list(e for e in dp if len(e) > 1)
