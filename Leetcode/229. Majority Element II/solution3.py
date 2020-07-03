class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = [0, 0]
        c2 = [0, 0]

        for n in nums:
            if n == c1[0]:
                c1[1] += 1
            elif n == c2[0]:
                c2[1] += 1
            elif c1[1] == 0:
                c1 = [n, 1]
            elif c2[1] == 0:
                c2 = [n, 1]
            else:
                c1[1] -= 1
                c2[1] -= 1

        return [x for x in {c1[0], c2[0]} if nums.count(x) > len(nums) / 3]
