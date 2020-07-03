class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)

        if l == 0: return []
        if l == 1: return [str(nums[0])]

        result = []

        i = 0

        while i < l:
            j = i

            while j < l - 1 and nums[j] == nums[j + 1] - 1: j += 1

            if j == i:
                result.append(str(nums[i]))
            else:
                result.append('%s->%s' % (str(nums[i]), str(nums[j])))

            i = j + 1

        return result
