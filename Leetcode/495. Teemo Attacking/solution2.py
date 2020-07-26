class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        curr = 0
        prev = timeSeries[0] if timeSeries else -1

        for t in timeSeries:
            if t - prev > duration:
                curr += duration
            else:
                curr += t - prev

            prev = t

        if prev >= 0: curr += duration

        return curr
