class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        h = {}

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum_ab = nums[i] + nums[j]
                if sum_ab not in h: h[sum_ab] = []
                h[sum_ab].append((i, j))

        result = set()

        for sum_ab in h:
            sum_cd = target - sum_ab
            if sum_cd in h:
                for a, b in h[sum_ab]:
                    for c, d in h[sum_cd]:
                        if a != c and a != d and b != c and b != d:
                            result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))

        return result
