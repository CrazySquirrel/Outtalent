class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(set(nums)) == len(nums): return False
        if k < 0 or t < 0: return False
        nums_sort = sorted(list(enumerate(nums)))
        for index1, num1 in nums_sort:
            for index2, num2 in nums_sort:
                if index1 == index2: continue
                if abs(index1 - index2) <= k and abs(num1 - num2) <= t: return True
        return False
