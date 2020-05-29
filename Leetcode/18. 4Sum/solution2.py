class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = set()

        n = len(nums)

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target: break
            if nums[a] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target: break
                if nums[a] + nums[b] + nums[n - 2] + nums[n - 1] < target: continue

                c, d = b + 1, n - 1

                rem_target = target - (nums[a] + nums[b])

                while c < d:
                    if nums[c] + nums[d] > rem_target:
                        d -= 1
                    elif nums[c] + nums[d] < rem_target:
                        c += 1
                    else:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1

        return result
