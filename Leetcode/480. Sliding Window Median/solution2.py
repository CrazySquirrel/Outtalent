from bisect import bisect_left, insort


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        result = [(window[k // 2] + window[(k - 1) // 2]) / 2]

        for i in range(k, len(nums)):
            window.pop(bisect_left(window, nums[i - k]))
            insort(window, nums[i])
            result.append((window[k // 2] + window[(k - 1) // 2]) / 2)

        return result
