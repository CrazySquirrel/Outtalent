from collections import Counter


class Solution:
    def threeSum(self, nums):
        counter = Counter(nums)
        result = [] if counter[0] < 3 else [[0, 0, 0]]
        ns, ps = [], []

        for x in counter:
            if x <= 0:
                ns.append(x)
            else:
                ps.append(x)

        for n in ns:
            for p in ps:
                x = -n - p
                if x in counter and (x in {n, p} and counter[x] > 1 or n < x < p):
                    result.append([n, x, p])

        return result
