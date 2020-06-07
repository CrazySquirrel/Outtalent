class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(i) for i in ''.join(map(str, nums)).split('0')])
