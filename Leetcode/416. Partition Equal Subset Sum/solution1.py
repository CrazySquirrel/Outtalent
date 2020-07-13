class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2

        if total % 2: return False

        nums.sort(reverse=True)

        dp = {0}

        for num in nums:
            new_sums = set()

            for i in dp:
                if num + i == target:
                    return True
                elif num + i < target:
                    new_sums.add(num + i)

            dp |= new_sums

        return False
