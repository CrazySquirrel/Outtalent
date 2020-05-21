class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [n for n in nums if n != val]
        return len(nums)
