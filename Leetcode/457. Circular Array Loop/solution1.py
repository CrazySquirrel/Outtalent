class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        for i, num in enumerate(nums):
            if num == 0: continue
            cur = i
            flag = num / abs(num)
            seen = set()
            while nums[cur] * flag > 0:
                nx = (cur + nums[cur]) % N
                nums[cur] = 0
                seen.add(cur)
                if nx in seen and cur != nx: return True
                cur = nx
        return False
