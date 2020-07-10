class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def factors(n):
            out = [1]
            for i in range(2, int(math.sqrt(n)) + 1):
                if not n % i:
                    out.append(i)
                    if i * i != n:
                        out.append(n // i)
            return out

        nums.sort()

        d = {}
        for n in nums:
            for e in factors(n):
                tmp = d.get(e, []) + [n]
                d[n] = tmp if len(d.get(n, [])) < len(tmp) else d.get(n, [])

        return nums and max(d.values(), key=len)
