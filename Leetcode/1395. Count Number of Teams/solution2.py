from bisect import bisect


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def insert(x):
            i = bisect(tmp, x)
            tmp.insert(i, x)
            return i

        tmp = []
        l = list(map(insert, rating))

        tmp = []
        g = list(map(insert, rating[::-1]))
        g.reverse()

        counter = 0

        total_length = len(rating)
        index_length = total_length - 1

        for i in range(total_length):
            counter += l[i] * (index_length - i - g[i])
            counter += g[i] * (i - l[i])

        return counter
