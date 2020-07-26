class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        seen = set()
        nums.sort(key=lambda x: -x)

        def dfs(i: int, nums: List[int], target: List[int]) -> bool:
            if tuple(sorted(target)) in seen:
                return False

            if all([m == 0 for m in target]):
                return True

            for j in range(4):
                if nums[i] <= target[j]:
                    if dfs(i + 1, nums, target[:j] + [target[j] - nums[i]] + target[j + 1:]):
                        return True

            seen.add(tuple(sorted(target)))

            return False

        total = sum(nums)

        if total % 4 or total == 0: return False

        total //= 4

        return dfs(0, nums, [total, total, total, total])
