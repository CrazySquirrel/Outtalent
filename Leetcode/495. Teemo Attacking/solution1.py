class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 0: return 0
        total = sum(min(timeSeries[i + 1] - timeSeries[i], duration) for i in range(n - 1))
        return total + duration
