class Solution:
    def threeSum(self, nums):
        counter = {}
        negative, positive = set(), set()

        for x in nums:
            if x not in counter:
                counter[x] = 0

            counter[x] += 1

            if x <= 0:
                negative.add(x)
            else:
                positive.add(x)

        result = set() if counter.get(0, 0) < 3 else {(0, 0, 0)}

        for n in negative:
            for p in positive:
                x = -n - p
                if x in counter and (x in {n, p} and counter[x] > 1 or n < x < p):
                    result.add((n, x, p))

        return result
