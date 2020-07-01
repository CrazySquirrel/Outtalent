class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for a1 in arr1:
            for a2 in arr2:
                if abs(a1 - a2) <= d: break
            else:
                result += 1
        return result
