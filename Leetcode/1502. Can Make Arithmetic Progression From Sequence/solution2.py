class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mn, mx = inf, -inf

        for n in arr:
            mn = min(mn, n)
            mx = max(mx, n)

        diff = (mx - mn) // (len(arr) - 1)

        if diff == 0: return True

        s = set(arr)

        for n in arr:
            if n != mx and (n + diff) not in s: return False

        return True
