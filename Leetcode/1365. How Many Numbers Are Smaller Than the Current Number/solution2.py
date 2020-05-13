class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        h = [0] * 101

        for num in nums:
            h[num] += 1

        prev = 0

        for i, num in enumerate(h):
            h[i] = prev
            prev += num

        return [h[num] for num in nums]