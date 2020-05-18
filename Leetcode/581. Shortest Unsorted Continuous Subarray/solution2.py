class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # check if sorted
        for start in range(0, len(nums) - 1):
            if nums[start] > nums[start + 1]: break
        else:
            return 0

        # find end
        end = len(nums) - 1
        while end > 0:
            if nums[end] < nums[end - 1]: break
            end -= 1

        # find min and max in unsorted part
        mx = mn = nums[start]
        for i in range(start + 1, end + 1):
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])

        # find true start
        for i in range(start):
            if nums[i] > mn:
                start = i
                break

        # find true end
        i = len(nums) - 1
        while i >= end + 1:
            if nums[i] < mx:
                end = i
                break
            i -= 1

        return end - start + 1