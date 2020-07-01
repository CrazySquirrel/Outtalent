class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for n, m in zip(heights, sorted(heights)):
            if n != m: count += 1
        return count
