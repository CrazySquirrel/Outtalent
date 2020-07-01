from statistics import mode


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) <= 9: return mode(arr)
        return mode([arr[int((len(arr) - 1) * ratio)] for ratio in [0.125 * i for i in range(9)]])
