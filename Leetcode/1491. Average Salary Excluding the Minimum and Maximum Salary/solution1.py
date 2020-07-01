class Solution:
    def average(self, salary: List[int]) -> float:
        mn = inf
        mx = -inf
        s = 0
        for n in salary:
            s += n
            mn = min(mn, n)
            mx = max(mx, n)
        return (s - mn - mx) / (len(salary) - 2)
