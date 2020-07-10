from bisect import bisect_left, insort


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median() -> int:
            return (window[k // 2] + window[k // 2 - 1]) / 2 if k % 2 == 0 else window[k // 2]

        window = sorted(nums[:k])
        result = [median()]

        for i in range(k, len(nums)):
            window.pop(bisect_left(window, nums[i - k]))
            insort(window, nums[i])
            result.append(median())

        return result
