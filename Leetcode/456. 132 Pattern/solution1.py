class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return False
        mid = -inf
        stack = []
        for n in nums[::-1]:
            if n < mid: return True
            while stack and stack[-1] < n: mid = stack.pop()
            stack.append(n)
        return False
