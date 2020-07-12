class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        two_sum = collections.defaultdict(list)

        for a in range(len(nums) - 1):
            for b in range(a + 1, len(nums)):
                two_sum[nums[a] + nums[b]].append((a, b))

        result = set()

        for sum_ab in two_sum:
            sum_cd = target - sum_ab

            if sum_cd not in two_sum: continue

            for a, b in two_sum[sum_ab]:
                for c, d in two_sum[sum_cd]:
                    if a != c and a != d and b != c and b != d:
                        result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))

        return result
