from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        l = len(arr2)

        arr2 = sorted(arr2)

        result = 0

        for a in arr1:
            i = bisect_left(arr2, a)

            if i == l:
                result += abs(a - arr2[-1]) > d
            elif i == 0:
                result += abs(a - arr2[0]) > d
            else:
                result += abs(a - arr2[i - 1]) > d and abs(a - arr2[i]) > d

        return result
