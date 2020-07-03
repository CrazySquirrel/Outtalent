class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = set()
        for n in nums:
            if n in result:
                result.remove(n)
            else:
                result.add(n)
        return result
